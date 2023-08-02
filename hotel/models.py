from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.geoip2 import GeoIP2




# Gestion des hôtels
class Hotel(models.Model):
    nom = models.CharField(max_length=100, default="Un nom par défaut")
    description = models.TextField(default="Une description par défaut", blank=True)
    logo = models.ImageField(upload_to='users/', null=True, blank=True)
    lieu = models.PointField(null=True, blank=True)
    ifu = models.CharField(max_length=20, default=None, null=True, blank=True)
    tel = models.CharField(max_length=20, default=None, null=True)
    mail = models.EmailField(max_length=254, unique=True, default=None, blank=True)
    site_web = models.URLField(max_length=200, null=True, blank=True)
    adresse = models.CharField(max_length=200, null=True, blank=True)
    pays = models.CharField(max_length=100, blank=True)
    ville = models.CharField(max_length=100, blank=True)
    code_postal = models.CharField(max_length=10, blank=True)
    region = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nom

    def save(self, *args, **kwargs):
        if self.lieu:
            # Utiliser geoip2 pour obtenir le map
            geoip = GeoIP2()
            geolocation = geoip.city(self.lieu)

            # Mettre les informations à jour
            self.adresse = geolocation.city
            self.pays = geolocation.country_name
            self.ville = geolocation.city
            self.code_postal = geolocation.postal_code
            self.region = geolocation.region

        super().save(*args, **kwargs)

