from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import (
    InventaireCuisine,
    LigneInventaireCuisine
)

from .serializers import (
    InventaireCuisineSerializer,
    LigneInventaireCuisineSerializer
)





# INVENTAIRE CUISINE
@api_view(['GET'])
def get_inventaire_cuisine(request):
    lignes = InventaireCuisine.objects.all()
    serialized_lignes = InventaireCuisineSerializer(lignes, many=True)
    return Response(serialized_lignes.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_inventaire_cuisine(request):
    serialized_data = InventaireCuisineSerializer(data=request.data)
    
    if serialized_data.is_valid():
        serialized_data.save()
        return Response(serialized_data.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)



# LIGNE INVENTAIRE CUISINE
@api_view(['GET'])
def get_lignes_inventaire_cuisine(request):
    lignes = LigneInventaireCuisine.objects.all()
    serialized_lignes = LigneInventaireCuisineSerializer(lignes, many=True)
    return Response(serialized_lignes.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_ligne_inventaire_cuisine(request):
    serialized_data = LigneInventaireCuisineSerializer(data=request.data)
    
    if serialized_data.is_valid():
        serialized_data.save()
        return Response(serialized_data.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

