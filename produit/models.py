from django.db import models




class Produit(models.Model):
    nom = models.CharField(max_length=100)
    prix_vente = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    
    def __str__(self):
        return self.nom

