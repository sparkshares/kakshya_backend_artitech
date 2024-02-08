from rest_framework.decorators import api_view, permission_classes

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from assignments.services.submit_assignment_service import submit_assignment_service

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def submit_assignment_view(request):
    data, status_code = submit_assignment_service(request.user, request.data)
    return Response(data, status=status_code)