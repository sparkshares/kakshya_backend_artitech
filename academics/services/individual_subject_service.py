from fastapi import Response
from rest_framework import status
from academics.models import Subject
from academics.models.subject_enrolled import SubjectEnrolled
from academics.serializers.individual_subject_serializer import IndividualSubjectSerializer  # replace with your actual Subject model

def individual_subject_service(user, data):
    try:
        # Fetch the subject from the database
        subject = Subject.objects.get(id=data['sub_id'])

        # Check if the user is enrolled in the subject
        if not SubjectEnrolled.objects.filter(sub_id=subject.id, student_id=user.student.id).exists():
            return {"error": "User is not enrolled in this subject"}, status.HTTP_400_BAD_REQUEST

        # Serialize the subject
        serializer = IndividualSubjectSerializer(subject)

        return serializer.data, status.HTTP_200_OK
    except Subject.DoesNotExist:
        return {"error": "Subject not found"}, status.HTTP_404_NOT_FOUND