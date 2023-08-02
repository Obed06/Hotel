from rest_framework import serializers
from .models import StockMagasin





class StockMagasinSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockMagasin
        fields = [
            "produit",
            "quantite"
        ]

