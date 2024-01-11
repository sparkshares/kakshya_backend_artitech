from rest_framework import status 

from django.core.exceptions import ObjectDoesNotExist

from academics.models.subject import Subject
from academics.serializers.subject_material_serializer import SubjectMaterialSerializer

def create_subject_material_service(user, data):
    try:
        # Get the subject instance using the sub_id
        subject = Subject.objects.get(id=data['sub_id'])
    except ObjectDoesNotExist:
        return {"error": "Subject with given sub_id does not exist"}, status.HTTP_400_BAD_REQUEST

    # Check if the subject was created by the same user
    if subject.teacher_id.user != user:
        return {"error": "You are not authorized to add material to this subject"}, status.HTTP_403_FORBIDDEN

    # Prepare the data for the serializer
    serializer_data = {
        'subm_title': data['subm_title'],
        'subm_description': data['subm_description'],
        'sub_filepath': data['sub_filepath'],
        'sub_id': subject.id,
    }

    serializer = SubjectMaterialSerializer(data=serializer_data)
    if serializer.is_valid():
        serializer.save()
        return serializer.data, status.HTTP_201_CREATED

    return serializer.errors, status.HTTP_400_BAD_REQUEST