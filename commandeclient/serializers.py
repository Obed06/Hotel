from rest_framework import serializers
from .models import (
	CommandeClient,
	LigneCommandeClient
)




class CommandeClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommandeClient
        fields = [
        	"produits",
        	"date_commande"
       ]


class LigneCommandeClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = LigneCommandeClient
        fields = [
        	"commande",
        	"quantite"
       ]

