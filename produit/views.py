from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Produit
from .serializers import ProduitSerializer




# PRODUIT
@api_view(['GET'])
def get_produits(request):
    produits = Produit.objects.all()
    serialized_produits = ProduitSerializer(produits, many=True)
    return Response(serialized_produits.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_produit(request):
    serialized_data = ProduitSerializer(data=request.data)
    
    if serialized_data.is_valid():
        serialized_data.save()
        return Response(serialized_data.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

