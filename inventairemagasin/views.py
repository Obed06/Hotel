from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import (
    InventaireMagasin,
    LigneInventaireMagasin
)

from .serializers import (
    InventaireMagasinSerializer,
    LigneInventaireMagasinSerializer
)




# INVENTAIRE MAGASIN
@api_view(['GET'])
def get_inventaire_magasin(request):
    lignes = InventaireMagasin.objects.all()
    serialized_lignes = InventaireMagasinSerializer(lignes, many=True)
    return Response(serialized_lignes.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_inventaire_magasin(request):
    serialized_data = InventaireMagasinSerializer(data=request.data)
    
    if serialized_data.is_valid():
        serialized_data.save()
        return Response(serialized_data.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)



# LIGNE INVENTAIRE MAGASIN
@api_view(['GET'])
def get_lignes_inventaire_magasin(request):
    lignes = LigneInventaireMagasin.objects.all()
    serialized_lignes = LigneInventaireMagasinSerializer(lignes, many=True)
    return Response(serialized_lignes.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_ligne_inventaire_magasin(request):
    serialized_data = LigneInventaireMagasinSerializer(data=request.data)
    
    if serialized_data.is_valid():
        serialized_data.save()
        return Response(serialized_data.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

