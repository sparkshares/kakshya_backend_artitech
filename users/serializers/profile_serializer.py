from rest_framework import serializers
from users.models.User import User

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "email", "name", "role","created_at"]