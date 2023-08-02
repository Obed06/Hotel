from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Compte
from .serializers import CompteSerializer




# COMPTE
@api_view(['GET'])
def get_comptes(request):
    comptes = Compte.objects.all()
    serialized_comptes = CompteSerializer(comptes, many=True)
    return Response(serialized_comptes.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_compte(request):
    serialized_data = CompteSerializer(data=request.data)
    
    if serialized_data.is_valid():
        serialized_data.save()
        return Response(serialized_data.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)