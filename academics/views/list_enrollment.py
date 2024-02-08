from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from academics.services.list_enrollment_service import list_enrollment_service

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def list_enrollment_view(request):
    data,status_code = list_enrollment_service(request.user)
    return Response(data,status=status_code)