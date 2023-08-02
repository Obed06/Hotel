from django.db import models
from django.utils import timezone
from userprofile.models import UserProfile
from chambre.models import Chambre
from service.models import Service




# Gestion des réservations
class Reservation(models.Model):
    utilisateur = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default=None, blank=True)
    chambre = models.ForeignKey(Chambre, on_delete=models.CASCADE, default=None, blank=True)
    services = models.ForeignKey(Service, on_delete=models.CASCADE, blank=True)
    date_service = models.DateField(default=timezone.now, blank=True)
    fin_service = models.DateField(default=timezone.now, blank=True)
    date_reservation = models.DateField(default=timezone.now)
    fin_reservation = models.DateField(default=timezone.now)
    is_available = models.BooleanField(default=False, blank=True)
    is_valid = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return f"Réservation de {self.chambre} pour le {self.date_reservation}"

