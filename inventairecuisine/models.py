from django.db import models
from django.utils import timezone
from produit.models import Produit




class InventaireCuisine(models.Model):
    date = models.DateField(default=timezone.now)
    produits = models.ForeignKey(Produit, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return f"Inventaire cuisine du {self.date}"




class LigneInventaireCuisine(models.Model):
    inventaire = models.ForeignKey(InventaireCuisine, on_delete=models.CASCADE)
    quantite = models.IntegerField()

    def __str__(self):
        return f"Ligne inventaire cuisine {self.inventaire.id} - {self.produit}"

