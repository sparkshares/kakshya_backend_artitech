from academics.models.subject import Subject
from academics.serializers.subject_serializer import SubjectSerializer
from rest_framework import status

def list_subject_service(user):
    subjects = Subject.objects.filter(teacher_id=user.teacher.id)
    serializer = SubjectSerializer(subjects, many=True)
    return serializer.data, status.HTTP_200_OK