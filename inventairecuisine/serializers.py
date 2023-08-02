from rest_framework import serializers
from .models import (
	InventaireCuisine,
	LigneInventaireCuisine
)




class LigneInventaireCuisineSerializer(serializers.ModelSerializer):
    class Meta:
        model = LigneInventaireCuisine
        fields = [
        	"inventaire",
        	"quantite"
        ]


class InventaireCuisineSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventaireCuisine
        fields = [
        	"date",
        	"produits"
        ]

