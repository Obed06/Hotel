from rest_framework import serializers
from .models import (
	CommandeFournisseur,
	LigneCommandeFournisseur
)




# COMMANDE FOURNISSEUR
class CommandeFournisseurSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommandeFournisseur
        fields = [
        	"fournisseur",
        	"date_livraison"
        ]




class LigneCommandeFournisseurSerializer(serializers.ModelSerializer):
    class Meta:
        model = LigneCommandeFournisseur
        fields = [
        	"produit",
        	"quantite"
        ]

