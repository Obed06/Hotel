from django.db import models
from produit.models import Produit




class StockCuisine(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.IntegerField()

    def __str__(self):
        return f"{self.produit.nom}"

