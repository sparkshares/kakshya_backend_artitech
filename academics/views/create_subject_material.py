from rest_framework.decorators import api_view, permission_classes

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from academics.services.create_subject_material_service import create_subject_material_service

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_subject_material_view(request):
    data, status_code = create_subject_material_service(request.user, request.data)
    return Response(data, status=status_code)