from django.db import models
from hotel.models import Hotel



# Types de chambre
class TypeChambre(models.Model):
    roomType = models.CharField(max_length=30, default=None, null=True)

    def __str__(self):
        return f"{self.roomType}"


# Type de lit
class TypeLit(models.Model):
    bedType = models.CharField(max_length=30, default=None, null=True)

    def __str__(self):
        return f"{self.bedType}"


# Gestion des chambres
class Chambre(models.Model):
    numero = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    type_chambre = models.ForeignKey(TypeChambre, on_delete=models.CASCADE, blank=True)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    nombre_lits = models.IntegerField()
    bedType = models.ForeignKey(TypeLit, on_delete=models.CASCADE, default=1, blank=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='chambres')

    def __str__(self):
        return f"{self.type_chambre}"

