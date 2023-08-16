from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework import status
from django.shortcuts import render
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from datetime import datetime, timedelta
from .models import UserProfile
from .serializers import UserProfileSerializer
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.http import JsonResponse





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

        if valide:
            return Response({'valide': valide}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password, email=email)
        users = User.objects.all()
        
        for user in users:
            if user.is_staff != True:
                user.is_staff = True
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






@api_view(['POST'])
@renderer_classes([JSONRenderer])
def generate_and_send_password(request):
    email = request.data.get('email')

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response({'detail': 'User not found'}, status=404)
    
    temp_password = get_random_string(length=12)  # Générez un mot de passe aléatoire
    
    # Envoi du mot de passe temporaire par e-mail
    try:
        subject = 'Votre nouveau mot de passe'
        message = f'Votre nouveau mot de passe temporaire est : {temp_password}'
        from_email = 'leonardovodouhe06@gmail.com'
        recipient_list = [email]

        send_mail(subject, message, from_email, recipient_list)
    except Exception as e:
        return Response({'detail': f'Failed to send email: {str(e)}'}, status=500)
    
    return Response({'detail': 'Password generated and sent'}, status=200)




@api_view(['POST'])
def change_password_with_temporary(request):
    email = request.data.get('email')
    temp_password = request.data.get('temp_password')
    new_password = request.data.get('new_password')
    
    try:
        profile = UserProfile.objects.get(email=email, temp_password=temp_password, temp_password_expiration__gt=datetime.now())
    except UserProfile.DoesNotExist:
        return Response({'detail': 'Invalid credentials or password expired'}, status=400)
    
    # Mettez à jour le mot de passe de l'utilisateur associé au profil
    user = profile.user
    user.set_password(new_password)
    user.save()

    # Effacez les champs de mot de passe temporaire
    profile.temp_password = None
    profile.temp_password_expiration = None
    profile.save()
    
    return Response({'detail': 'Password changed successfully'})




# Changer mot de passe par mail
def do_mail_password(request):
    return render(request, "userprofile/mail_password.html")
