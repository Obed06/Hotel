from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Notification
from .serializers import NotificationSerializer




# NOTIFICATION
@api_view(['GET'])
def get_notification(request):
    notifications = Notification.objects.all()
    serialized_notifications = NotificationSerializer(notifications, many=True)
    return Response(serialized_notifications.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_notification(request):
    serializer = NotificationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

