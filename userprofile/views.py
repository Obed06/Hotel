from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, logout, authenticate, login
from rest_framework import status

from .models import UserProfile
from .serializers import UserProfileSerializer
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view

from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail
from datetime import timedelta

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.http import JsonResponse

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.utils import timezone

from rest_framework.decorators import api_view
from rest_framework.response import Response
import secrets
import string

from django.contrib.auth.hashers import make_password, check_password, PBKDF2PasswordHasher
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes

from django.db import IntegrityError
import hashlib
import os





# TESTER ETAT DE LA CONNEXION
@api_view(['POST'])
def login_view(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return Response({'message': "Connexion réussie."}, status=status.HTTP_200_OK)
        else:
            return Response({'message': "Identifiant ou mot de passe incorrect."}, status=status.HTTP_401_UNAUTHORIZED)





# LISTE UTILISATEUR
@api_view(['GET'])
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        user_data = []
        for user in users:
            user_data.append({
                'Nom': user.username,
                'Mot de passe': user.password,
                'E-mail': user.email,
                'Equipe': user.is_staff,
                'Super': user.is_superuser
            })
        return Response(user_data, status=status.HTTP_200_OK)




# INSCRIPTION
class RegisterView(APIView):
    def post(self, request):
        if request.method == 'POST':
            username = request.POST.get('nom')
            password = request.POST.get('password')
            confirm = request.POST.get('confirm')
            email = request.POST.get('mail')

        valide = {}
        if password != confirm:
            valide['confirm'] = "Les mots de passe ne correspondent pas."

        elif get_user_model().objects.filter(username=username).exists():
            valide['username'] = "Ce nom d'utilisateur est déjà pris."

        elif valide:
            return Response({'valide': valide}, status=status.HTTP_400_BAD_REQUEST)

        # Créer un nouvel utilisateur en spécifiant l'adresse e-mail
        user = get_user_model().objects.create_user(username=username, password=password, email=email)

        # Créer ou mettre à jour le profil utilisateur
        user_profile, created = UserProfile.objects.get_or_create(user=user)
        
        if not user.is_staff or not user.is_superuser:
            user.is_staff = True
            user.is_superuser = True
            user.save()
        
        return Response({'Message': 'Utilisateur créé avec succès.'}, status=status.HTTP_201_CREATED)




# MAIL UTILISATEUR
@api_view(['GET'])
def get_email(request):
    Users = User.objects.all()
    Email = []
    for i in Users:
        Email.append({
            "nom": i.username,
            "mail": i.email
        })
    return Response(Email, status=200)




# TRANSFORMER ETAT DE CHAQUE UTILISATEUR (STATUT-EQUIPE & STATUT-SUPERUSER)
@api_view(['GET'])
def set_staff_and_superuser(request):
    Users = User.objects.all()
    for user in Users:
        if not user.is_staff or not user.is_superuser:
            user.is_staff = True
            user.is_superuser = True
        user.save()
    return Response("Modification effectuée avec succès !", status=200)




# DESACTIVER USERS SAUF LE PREMIER UTILISATEUR
@api_view(['GET','POST'])
def disable_user(request):
    username = request.data.get('username')
    User = get_user_model()

    try:
        user = User.objects.get(username=username)
    except UserProfile.DoesNotExist:
        return Response({'message': "Le profil de l'utilisateur est introuvable."}, status=status.HTTP_404_NOT_FOUND)

    user.is_active = False
    user.save()
    return Response({'message': "L'utilisateur désactivé avec succès."}, status=status.HTTP_200_OK)



def inscription_page(request):
    return render(request, "userprofile/inscription.html")




# USERPROFILE
@api_view(['GET'])
def get_user_profiles(request):
    user_profiles = UserProfile.objects.all()
    serialized_profiles = UserProfileSerializer(user_profiles, many=True)
    return Response(serialized_profiles.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_user_profile(request):
    serialized_data = UserProfileSerializer(data=request.data)
    
    if serialized_data.is_valid():
        serialized_data.save()
        return Response(serialized_data.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)





def custom_logout(request):
    logout(request)
    # Rediriger vers la page de connexion de Django après la déconnexion
    return redirect('admin:login')




@api_view(['POST'])
def generate_password_and_send_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        # Vérifier si l'e-mail existe dans la base de données
        try:
            user = get_user_model().objects.get(email=email)
        except get_user_model().DoesNotExist:
            return Response({"message": "L'e-mail n'existe pas dans la base de données."}, status=400)

        # Générer un mot de passe aléatoire de 20 caractères
        password_length = 20 
        characters = string.ascii_letters + string.digits + string.punctuation
        generated_password = ''.join(secrets.choice(characters) for _ in range(password_length))

        # Générer un sel aléatoire (utiliser la fonction de Django)
        salt = None

        # Hacher le mot de passe généré avec l'algorithme SHA-2
        hashed_generated_password = make_password(generated_password, salt=salt)

        # Enregistrer le mot de passe haché comme ancien mot de passe pour l'utilisateur
        user.set_password(hashed_generated_password)
        user.save()


        # Obtenir l'heure actuelle
        current_time = timezone.now()

        # Calculer l'heure d'expiration (360 secondes plus tard)
        expiration_time = current_time + timezone.timedelta(seconds=420)

        # Construire le message de l'e-mail avec le mot de passe généré (non haché)
        subject = "Demande de réinitialisation de mot de passe"
        
        message = f"Bonjour,\
\n\nVous avez demandé la réinitialisation de votre mot de passe. Votre nouveau mot de passe temporaire est le suivant :\
\n\n{generated_password}\n\nLa page de réinitialisation s'est déjà affiché dans votre navigateur. Veuillez à renseigner tous les champs requis."

        from_email = "noreply@example.com"
        recipient_list = [email]

        # Envoyer l'e-mail
        send_mail(subject, message, from_email, recipient_list)

        response_data = {
            "message": "Un e-mail a été envoyé avec les instructions de réinitialisation.",
            "password": generated_password,
            "expiration_time": expiration_time,
        }

        return redirect('reset_password/', status=200)





@api_view(['POST'])
def temporary_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_new_password = request.POST.get('confirm_new_password')

        try:
            user = get_user_model().objects.get(email=email)
        except get_user_model().DoesNotExist:
            return Response({"message": "L'utilisateur avec cet e-mail n'existe pas."}, status=400)


        # Vérifier si le nouveau mot de passe et le mot de passe de confirmation correspondent
        if new_password != confirm_new_password:
            return Response({"message": "Les nouveaux mots de passe ne correspondent pas."}, status=400)

        # Vérifier si le nouveau mot de passe est différent de l'ancien mot de passe
        if new_password == old_password:
            return Response({"message": "Le nouveau mot de passe doit être différent de l'ancien mot de passe."}, status=400)

        # Mettre à jour le mot de passe de l'utilisateur avec le nouveau mot de passe saisi
        user.set_password(new_password)
        user.save()
            
    return Response({"message": "Le mot de passe a été mis à jour avec succès."}, status=200)
      





def submit_email(request):
    return render(request, 'userprofile/submit_email.html', status=200)


def reset_password(request):
    return render(request, 'userprofile/reset_password.html', status=200)


