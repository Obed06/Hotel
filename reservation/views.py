from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Reservation
from .serializers import ReservationSerializer




# RESERVATION
@api_view(['GET'])
def get_reservations(request):
    reservations = Reservation.objects.all()
    serialized_reservations = ReservationSerializer(reservations, many=True)
    return Response(serialized_reservations.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_reservation(request):
    serialized_data = ReservationSerializer(data=request.data)
    
    if serialized_data.is_valid():
        serialized_data.save()
        return Response(serialized_data.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)