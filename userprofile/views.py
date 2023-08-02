from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework import status
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserProfile
from .serializers import UserProfileSerializer




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
    users = User.objects.all()
    user_state = []
    for user in users:
        user_state.append({
            "id": user.id,
            "nom": user.username,
            "actif": user.is_active,
            "equipe": user.is_staff,
            "super": user.is_superuser
        })
        
        taille = len(user_state)
        T = taille - 1
        
        if T >= 0:
            if user_state[T]["nom"] == "root":
                pass
            else:
                user_state[T]["actif"] = False
                T-=1
    return Response(user_state, status=200)




def inscription_page(request):
    return render(request, "userprofile/inscription.html")




# GET ET POST DE CHAQUE MODELE
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