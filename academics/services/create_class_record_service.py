from rest_framework import status 

from django.core.exceptions import ObjectDoesNotExist

from academics.models.subject import Subject
from academics.serializers.class_record_serializer import ClassRecordSerializer
import os

from academics.tasks import create_class_record_task

def create_class_record_service(user,data):
    try:
        subject = Subject.objects.get(id =data["sub_id"])
    except ObjectDoesNotExist:
        return {"error":"Subject with given sub_id doesn't exist"},status.HTTP_400_BAD_REQUEST
    
    if subject.teacher_id.user!=user:
        return {"error":"You are not authorized to add class record to this subject"},status.HTTP_403_FORBIDDEN
    
    audio_file = data['audio_path']
    audio_extensions = ['.wav', '.mp3', '.aac', '.ogg', '.flac', '.m4a', '.wma']
    file_name, file_extension = os.path.splitext(audio_file.name)

    if file_extension not in audio_extensions:
        return {"error": "The provided file is not an audio file"}, status.HTTP_400_BAD_REQUEST

    # If the filename is longer than 100 characters, keep only the last 100 characters
    if len(audio_file.name) > 100:
        audio_file.name = file_name[:100-len(file_extension)] + file_extension
    
    serializer_data = {
        'class_title': data['class_title'],
        'class_description': data['class_description'],
        'audio_path': data['audio_path'],
        'sub_id': subject.id
    }

    serializer = ClassRecordSerializer(data=serializer_data)
    if serializer.is_valid():
        serializer.save()
        record_id = serializer.instance.id
        record_file_path = serializer.instance.audio_path.path
        
        create_class_record_task.delay(record_id, record_file_path)
        response_data = serializer.data
        response_data['summary_status'] = "The audio is processing, once completed it will be shown to your dashboard"
        return response_data, status.HTTP_201_CREATED
    
    return serializer.errors,status.HTTP_400_BAD_REQUEST