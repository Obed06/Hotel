from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Service
from .serializers import ServiceSerializer 




# SERVICES
@api_view(['GET'])
def get_services(request):
    services = Service.objects.all()
    serialized_services = ServiceSerializer(services, many=True)
    return Response(serialized_services.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_service(request):
    serialized_data = ServiceSerializer(data=request.data)
    
    if serialized_data.is_valid():
        serialized_data.save()
        return Response(serialized_data.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

