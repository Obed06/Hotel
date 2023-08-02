from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Hotel
from .serializers import HotelSerializer




# HOTEL
@api_view(['GET'])
def get_hotels(request):
    hotels = Hotel.objects.all()
    serialized_hotels = HotelSerializer(hotels, many=True)
    return Response(serialized_hotels.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_hotel(request):
    serialized_data = HotelSerializer(data=request.data)
    
    if serialized_data.is_valid():
        serialized_data.save()
        return Response(serialized_data.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

