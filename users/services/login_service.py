from django.contrib.auth import authenticate
from rest_framework import status
from users.serializers.login_serializer import LoginSerializer 
from users.services.register_service import get_token_for_user


    
def login_service(data):
    serializer = LoginSerializer(data=data)
    if serializer.is_valid():
        email = serializer.data.get("email")
        password = serializer.data.get("password")
        user = authenticate(email=email, password=password)
        
        if user is not None:
            token = get_token_for_user(user)
            return {"token":token,"msg":"Login Successful"},status.HTTP_200_OK
        return {"msg":"Invalid Credentials"},status.HTTP_401_UNAUTHORIZED
    return serializer.errors,status.HTTP_400_BAD_REQUEST