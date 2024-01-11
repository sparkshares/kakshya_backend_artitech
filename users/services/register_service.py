from django.contrib.auth import authenticate

from rest_framework import status
from users.serializers.register_serializers import RegistrationSerializer 
from users.services.helper.get_token import get_token_for_user

    
def register_service(data):
    serializer = RegistrationSerializer(data=data)
    
    if serializer.is_valid():
        user = serializer.save()
        token = get_token_for_user(user)
        return {"token":token,"msg":"Registration Successful"},status.HTTP_201_CREATED
    return serializer.errors,status.HTTP_400_BAD_REQUEST