from django.db import models




# Gestion des types de services
class Service(models.Model):
    nom = models.CharField(max_length=100, default=None)
    prix = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return self.nom

