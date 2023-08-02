from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import (
	CommandeClient,
	LigneCommandeClient
)

from .serializers import (
	CommandeClientSerializer,
	LigneCommandeClientSerializer
)




# COMMANDE CLIENT
@api_view(['GET'])
def get_commandes_clients(request):
    commandes = CommandeClient.objects.all()
    serialized_commandes = CommandeClientSerializer(commandes)
    return Response(serialized_commandes.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_commande_client(request):
    serialized_data = CommandeClientSerializer(data=request.data)
    
    if serialized_data.is_valid():
        serialized_data.save()
        return Response(serialized_data.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)




# LIGNE COMMANDE CLIENT
@api_view(['GET'])
def get_lignes_commande_client(request):
    lignes = LigneCommandeClient.objects.all()
    serialized_lignes = LigneCommandeClientSerializer(lignes)
    return Response(serialized_lignes.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_ligne_commande_client(request):
    serialized_data = LigneCommandeClientSerializer(data=request.data)
    
    if serialized_data.is_valid():
        serialized_data.save()
        return Response(serialized_data.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

