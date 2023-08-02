from django.db import models
from django.utils import timezone
from produit.models import Produit




class CommandeFournisseur(models.Model):
    fournisseur = models.CharField(max_length=100)
    date_livraison = models.DateField(default=timezone.now)
    date_commande = models.DateField(default=timezone.now, blank=True)

    def __str__(self):
        return f"{self.fournisseur}"




class LigneCommandeFournisseur(models.Model):
    commande = models.ForeignKey(CommandeFournisseur, on_delete=models.CASCADE, blank=True)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, default=1)
    quantite = models.IntegerField()
    prix_vente = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, blank=True)

    def __str__(self):
        return f"{self.commande}\t------\t{self.produit}"

