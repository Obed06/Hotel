from django.db import models
from django.contrib.auth import get_user_model




# Gestion des profiles
class UserProfile(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    ifu = models.CharField(max_length=20, default=None, null=True, blank=True)
    photo = models.ImageField(upload_to='users/', null=True, blank=True)
    phone_number = models.CharField(max_length=20, default=None, null=True)
    address = models.TextField(default=None, null=True, blank=True)
    email = models.EmailField(max_length=254, unique=True, default=None, blank=True)
    speciality = models.CharField(max_length=100, default=None, null=True, blank=True)
    years_of_experience = models.IntegerField(default=0, null=True)
    grade = models.CharField(max_length=50, default=None, null=True, blank=True)
    job_title = models.CharField(max_length=100, default="Cuisinier")
    
    def __str__(self):
        return str(self.user)