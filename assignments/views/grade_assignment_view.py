from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from assignments.services.grade_assignment_service import grade_assignment_service

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def grade_assignment_view(request):
    data, status_code = grade_assignment_service(request.user, request.data)
    return Response(data, status=status_code)