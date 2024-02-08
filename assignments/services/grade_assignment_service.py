from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist

from assignments.models.assignment_transaction import AssignmentTransaction
from assignments.models import assignment_grading
from assignments.serializers.assignment_grading_serializer import AssignmentGradingSerializer
from users.models import User
from assignments.models import AssignmentGrading  # make sure to import the AssignmentGrading model
def grade_assignment_service(user, data):
    try:
        assignment = AssignmentTransaction.objects.get(id=data['as_trans_id'])
    except ObjectDoesNotExist:
        return {"error": "Assignment with given as_id doesn't exist"}, status.HTTP_400_BAD_REQUEST

    if user.role != User.TEACHER:
        return {"error": "Only teachers can grade assignments"}, status.HTTP_403_FORBIDDEN
    
    # Check if the user is the teacher of the subject of the assignment
    if assignment.as_id.sub_id.teacher_id.user != user:
        return {"error": "You are not authorized to grade this assignment"}, status.HTTP_403_FORBIDDEN

    if AssignmentGrading.objects.filter(as_trans_id=assignment).exists():
        return {"error": "This assignment has already been graded"}, status.HTTP_400_BAD_REQUEST

    grading_data = {
        "as_trans_id": data['as_trans_id'],
        "grade": data['grade'],
        "remark": data['remark'],
    }
    grading_serializer = AssignmentGradingSerializer(data=grading_data)
    if grading_serializer.is_valid():
        grading_serializer.save()

        # Update the status of the AssignmentTransaction to "Graded"
        assignment.status = "Graded"
        assignment.save()

        return grading_serializer.data, status.HTTP_201_CREATED
    else:
        return {"error": grading_serializer.errors}, status.HTTP_400_BAD_REQUEST