
from academics.models.subject import Subject
from academics.serializers.subject_serializer import SubjectSerializer
from rest_framework import status

def create_subject_service(user, data):
    data['teacher_id'] = user.teacher.id  # Set u_id to the id of the user's teacher profile
    serializer = SubjectSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return serializer.data, status.HTTP_201_CREATED
    return serializer.errors, status.HTTP_400_BAD_REQUEST
