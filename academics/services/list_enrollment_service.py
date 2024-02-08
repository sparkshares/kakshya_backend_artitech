from rest_framework import status

from academics.models.subject_enrolled import SubjectEnrolled
from academics.serializers.list_enrollment_serializer import ListEnrollmentSerializer

def list_enrollment_service(user):
    enrollment = SubjectEnrolled.objects.filter(student_id=user.student.id)
    serializer = ListEnrollmentSerializer(enrollment, many=True)
    return serializer.data, status.HTTP_200_OK