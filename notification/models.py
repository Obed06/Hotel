from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model




# NOTIFICATION
class Notification(models.Model):
    date = models.DateField(default=timezone.now)
    user_profile = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    message = models.CharField(max_length=500)
    reading = models.BooleanField(default=False)
    
    def __str__(self):
        return self.message

