from django.db import models
from django.utils import timezone
from reservation.models import Reservation
from commandeclient.models import LigneCommandeClient
from compte.models import Compte




# Gestion des Transactions
class Transaction(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, null=True, blank=True)
    date_transaction = models.DateField(default=timezone.now)
    lignecommandeclient = models.ForeignKey(LigneCommandeClient, on_delete=models.CASCADE, null=True, blank=True)
    compte = models.ForeignKey(Compte, on_delete=models.CASCADE, blank=True)
    montant = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Transaction de {self.montant} pour le compte {self.compte}"

