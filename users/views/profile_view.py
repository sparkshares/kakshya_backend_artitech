from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from users.services.profile_service import profile_change_password_service, profile_edit_service, profile_view_service


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def profile_get_view(request):
    # request.user gets the authenticated user's data
    data, status_code = profile_view_service(request.user)
    return Response(data, status=status_code)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def profile_edit_view(request):
    data, status_code = profile_edit_service(request.user, request.data)
    return Response(data, status=status_code)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def profile_change_password_view(request):
    data, status_code = profile_change_password_service(request.user, request.data)
    return Response(data, status=status_code)