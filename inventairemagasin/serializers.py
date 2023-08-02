from rest_framework import serializers
from .models import (
    InventaireMagasin,
    LigneInventaireMagasin
)




class LigneInventaireMagasinSerializer(serializers.ModelSerializer):
    class Meta:
        model = LigneInventaireMagasin
        fields = [
            "inventaire",
            "quantite_reel",
            "quantite_virtuel"
        ]


class InventaireMagasinSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventaireMagasin
        fields = [
            "date",
            "produits"
        ]

