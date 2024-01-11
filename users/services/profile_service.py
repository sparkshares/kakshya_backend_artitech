
from users.serializers.change_password_serializer import ChangePasswordSerializer
from users.serializers.profile_serializer import ProfileSerializer
from rest_framework import status


def profile_view_service(user):
    serializer = ProfileSerializer(user)
    return serializer.data,status.HTTP_200_OK

def profile_edit_service(user,data):
    serializer = ProfileSerializer(user,data=data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return serializer.data,status.HTTP_200_OK
    return serializer.errors,status.HTTP_400_BAD_REQUEST

def profile_change_password_service(user, data):
    serializer = ChangePasswordSerializer(data=data)
    if serializer.is_valid():
        old_password = data.get("old_password")
        new_password = data.get("new_password")
        print(f"Old password provided: {old_password}")
        print(f"Is old password correct: {user.check_password(old_password)}")
        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            return {"msg": "Password Changed Successfully"}, status.HTTP_200_OK
        else:
            return {"msg": "Invalid Old Password"}, status.HTTP_400_BAD_REQUEST
    else:
        return serializer.errors, status.HTTP_400_BAD_REQUEST