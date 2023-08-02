from rest_framework import serializers
from .models import Checkout




class CheckoutSerializer(serializers.ModelSerializer):
	class Meta:
		model = Checkout
		fields = [
			"datePay",
			"whoPay"
		]

