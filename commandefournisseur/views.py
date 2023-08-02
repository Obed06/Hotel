from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import (
    CommandeFournisseur,
    LigneCommandeFournisseur
)

from .serializers import (
    CommandeFournisseurSerializer,
    LigneCommandeFournisseurSerializer
)




@api_view(['GET'])
def get_commandes_fournisseurs(request):
    commandes = CommandeFournisseur.objects.all()
    serialized_commandes = CommandeFournisseurSerializer(commandes, many=True)
    return Response(serialized_commandes.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_commande_fournisseur(request):
    serialized_data = CommandeFournisseurSerializer(data=request.data)
    
    if serialized_data.is_valid():
        serialized_data.save()
        return Response(serialized_data.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET'])
def get_ligne_commandes_fournisseurs(request):
    commandes = LigneCommandeFournisseur.objects.all()
    serialized_commandes = LigneCommandeFournisseurSerializer(commandes, many=True)
    return Response(serialized_commandes.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_ligne_commande_fournisseur(request):
    serialized_data = LigneCommandeFournisseurSerializer(data=request.data)
    
    if serialized_data.is_valid():
        serialized_data.save()
        return Response(serialized_data.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

