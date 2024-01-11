from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from academics.models.subject_enrolled import SubjectEnrolled
from assignments.background_task.create_assignment_transaction_text_task import create_assignment_transaction_text_task
from users.models import User
import os

from assignments.models.assignment import Assignment
from assignments.serializers.assignment_transaction_serializer import AssignmentTransactionSerializer

def submit_assignment_service(user, data):
    try:
        assignment = Assignment.objects.get(id=data['as_id'])
    except ObjectDoesNotExist:
        return {"error": "Assignment with given as_id doesn't exist"}, status.HTTP_400_BAD_REQUEST

    if user.role != User.STUDENT:
        return {"error": "Only students can submit assignments"}, status.HTTP_403_FORBIDDEN

    if not SubjectEnrolled.objects.filter(sub_id=assignment.sub_id, student_id=user.student).exists():
        return {"error": "The student is not enrolled in this subject"}, status.HTTP_403_FORBIDDEN

    serializer_data = {
        'as_id': assignment.id,
        'as_trans_path': data['as_trans_path'],
        'submitted_by': user.student.id,
        'status': 'Submitted'
    }

    serializer = AssignmentTransactionSerializer(data=serializer_data)
    if serializer.is_valid():
        serializer.save()
        
        at_id = serializer.instance.id
        ast_path = serializer.instance.as_trans_path.path
        create_assignment_transaction_text_task.delay(at_id, ast_path)
        response_data = serializer.data
        response_data['assignment_status'] = "The assignment material is processing"
        return response_data, status.HTTP_201_CREATED

    return serializer.errors, status.HTTP_400_BAD_REQUEST