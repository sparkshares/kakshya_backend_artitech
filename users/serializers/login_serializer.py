from rest_framework import serializers
from users.models import User


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    class Meta:
        model = User
        fields = ["email", "password"]
      
