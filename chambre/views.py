from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Chambre
from .serializers import ChambreSerializer




# CHAMBRE
@api_view(['GET'])
def get_chambres(request):
    chambres = Chambre.objects.all()
    serialized_chambres = ChambreSerializer(chambres, many=True)
    return Response(serialized_chambres.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_chambre(request):
    serialized_data = ChambreSerializer(data=request.data)
    
    if serialized_data.is_valid():
        serialized_data.save()
        return Response(serialized_data.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

