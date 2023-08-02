from rest_framework import serializers
from .models import StockCuisine




class StockCuisineSerializer(serializers.ModelSerializer):
	class Meta:
		model = StockCuisine
		fields = [
			"produit",
			"quantite"
		]