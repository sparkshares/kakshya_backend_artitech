from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from academics.services.enroll_subject_service import enroll_subject_service


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def enroll_subject_view(request):
    data, status_code = enroll_subject_service(request.user, request.data)
    return Response(data, status=status_code)