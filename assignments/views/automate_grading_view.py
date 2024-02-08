from rest_framework.decorators import api_view, permission_classes

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from assignments.services.automate_grading_service import automate_grading_service


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def automate_grading_view(request):
    data, status_code = automate_grading_service(request.user, request.data)
    return Response(data, status=status_code)