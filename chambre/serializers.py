from rest_framework import serializers
from .models import Chambre
from hotel.models import Hotel




class ChambreSerializer(serializers.ModelSerializer):
	class Meta:
		model = Chambre
		fields = [
			"numero",
			"prix",
			"nombre_lits",
			"hotel"
		]

