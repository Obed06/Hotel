from django.db import models
from django.utils import timezone
from reservation.models import Reservation
from produit.models import Produit




class CommandeClient(models.Model):
    client = models.ForeignKey(Reservation, on_delete=models.CASCADE, blank=True)
    produits = models.ForeignKey(Produit, on_delete=models.CASCADE)
    date_commande = models.DateField(default=timezone.now)

    def __str__(self):
        return f"Date de commande:\t{self.date_commande}\n\
Produit:\t{self.produits}"




class LigneCommandeClient(models.Model):
    commande = models.ForeignKey(CommandeClient, on_delete=models.CASCADE, blank=True)
    quantite = models.IntegerField()
    
    def __str__(self):
        return f"Commande:\t{self.commande}"

