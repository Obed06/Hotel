from django.db import models
from userprofile.models import UserProfile




class Compte(models.Model):
    numero = models.CharField(max_length=20, unique=True)
    nom = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

