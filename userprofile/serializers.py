from rest_framework import serializers
from .models import UserProfile




class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            "user",
            "phone_number",
            "years_of_experience",
            "job_title",
            "email"
        ]

