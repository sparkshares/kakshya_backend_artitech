from rest_framework import serializers
from users.models import User

class RegistrationSerializer(serializers.ModelSerializer):
    
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    
    class Meta:
         model = User
         fields = ['email', 'name', 'password', 'password2','role']
         extra_kwargs = {
             'password': {'write_only': True}
         }

    def validate(self, data):
        password = data.get('password')
        password2 = data.get('password2')
        if password != password2:
            raise serializers.ValidationError("Passwords must match.")
        return data

    def create(self, validated_data):
        
        return User.objects.create_user(**validated_data)