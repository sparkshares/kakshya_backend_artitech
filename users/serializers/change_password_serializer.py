from rest_framework import serializers
from users.models import User



class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=255, write_only=True)
    new_password = serializers.CharField(max_length=255, min_length=6, write_only=True)
    new_password2 = serializers.CharField(max_length=255, min_length=6, write_only=True)

    def validate(self, attrs):
        new_password = attrs.get('new_password')
        new_password2 = attrs.get('new_password2')
        if new_password != new_password2:
            raise serializers.ValidationError("New passwords must match.")
        return attrs