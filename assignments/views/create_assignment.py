from rest_framework.decorators import api_view, permission_classes

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from assignments.services.create_assignment_service import create_assignment_service


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_assignment_view(request):
    data, status_code = create_assignment_service(request.user, request.data)
    return Response(data, status=status_code)