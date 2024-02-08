from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from academics.models.subject import Subject
from academics.models.subject_enrolled import SubjectEnrolled

from academics.serializers.enroll_subject_serializer import SubjectEnrolledSerializer 

def enroll_subject_service(user, data):
    try:
        subject = Subject.objects.get(sub_code = data['sub_code'])
    except ObjectDoesNotExist:
        return {"error":"Subject with given sub_code doesn't exist"}, status.HTTP_400_BAD_REQUEST

    # Check if the subject is already enrolled
    if SubjectEnrolled.objects.filter(sub_id=subject.id, student_id=user.student.id).exists():
        return {"error": "Subject is already enrolled"}, status.HTTP_400_BAD_REQUEST

    serializer_data = {
        'sub_id': subject.id,
        'student_id':user.student.id
    }

    serializer = SubjectEnrolledSerializer(data=serializer_data)
    if serializer.is_valid():
        serializer.save()
        return serializer.data, status.HTTP_201_CREATED

    return serializer.errors, status.HTTP_400_BAD_REQUEST