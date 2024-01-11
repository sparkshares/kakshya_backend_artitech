from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from academics.models.subject import Subject
from assignments.background_task.create_assignment_task import create_assignment_text_task
from assignments.serializers.assignment_serializer import AssignmentSerializer
import os

def create_assignment_service(user, data):
    try:
        subject = Subject.objects.get(id=data['sub_id'])
    except ObjectDoesNotExist:
        return {"error": "Subject with given sub_id doesn't exist"}, status.HTTP_400_BAD_REQUEST

    if subject.teacher_id.user != user:
        return {"error": "You are not authorized to create an assignment for this subject"}, status.HTTP_403_FORBIDDEN

    assignment_file = data['as_filepath']
    valid_extensions = ['.pdf', '.pptx', '.doc', '.docx', '.png', '.jpg', '.jpeg']
    file_extension = os.path.splitext(assignment_file.name)[1]

    if file_extension not in valid_extensions:
        return {"error": "The provided file format is not supported"}, status.HTTP_400_BAD_REQUEST

    serializer_data = {
        'as_title': data['as_title'],
        'as_description': data['as_description'],
        'as_filepath': data['as_filepath'],
        'sub_id': subject.id
    }

    serializer = AssignmentSerializer(data=serializer_data)
    if serializer.is_valid():
        serializer.save()
        
        a_id = serializer.instance.id
        as_path = serializer.instance.as_filepath.path
        create_assignment_text_task.delay(a_id, as_path)
        response_data = serializer.data
        response_data['assignment_status'] = "The assignment text is processing"
        return response_data, status.HTTP_201_CREATED

    return serializer.errors, status.HTTP_400_BAD_REQUEST