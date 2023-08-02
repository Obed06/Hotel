from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Checkout
from .serializers import CheckoutSerializer




# NOTIFICATION
@api_view(['GET'])
def get_checkout(request):
    check = Checkout.objects.all()
    serialized_check = CheckoutSerializer(check, many=True)
    return Response(serialized_notifications.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_checkout(request):
    serializer = CheckoutSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

