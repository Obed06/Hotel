from django.db import models
from django.utils import timezone
from produit.models import Produit




class InventaireMagasin(models.Model):
    date = models.DateField(default=timezone.now)
    produits = models.ForeignKey(Produit, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"Inventaire magasin du\t==>\t{self.date}"




class LigneInventaireMagasin(models.Model):
    inventaire = models.ForeignKey(InventaireMagasin, on_delete=models.CASCADE, blank=True)
    quantite_reel = models.IntegerField(default=0)
    quantite_virtuel = models.IntegerField(default=0)
    motif = models.CharField(max_length=100, default=None, blank=True)

    def __str__(self):
        return f"Ligne inventaire magasin {self.inventaire.id} - {self.produit.nom}"

