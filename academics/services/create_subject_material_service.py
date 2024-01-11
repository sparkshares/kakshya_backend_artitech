import os
from rest_framework import status 

from django.core.exceptions import ObjectDoesNotExist
from academics.background_task.create_material_summary_task import create_material_summary_task

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

    # Check the file format
    allowed_extensions = ['.pdf', '.doc', '.docx', '.ppt', '.pptx']
    file_extension = os.path.splitext(data['sub_filepath'].name)[1]
    if file_extension not in allowed_extensions:
        return {"error": "Unsupported file format. Please upload a PDF, Word document, or text file."}, status.HTTP_400_BAD_REQUEST

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
        sub_mat_id = serializer.instance.id
        sub_filepath = serializer.instance.sub_filepath.path
        
        create_material_summary_task.delay(sub_mat_id, sub_filepath)
        response_data = serializer.data
        response_data['summary_status'] = "The subject material is processing, once completed you will be able to chat"
        return response_data, status.HTTP_201_CREATED

    return serializer.errors, status.HTTP_400_BAD_REQUEST