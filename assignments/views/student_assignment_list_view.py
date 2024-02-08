from rest_framework.decorators import api_view, permission_classes

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from assignments.services.student_assignment_list_service import student_assignment_list_service

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def student_assignment_list_view(request):
    data,status_code = student_assignment_list_service(request.user)
    return Response(data,status=status_code)