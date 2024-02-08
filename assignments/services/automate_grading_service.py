from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from academics.models.subject import Subject
from assignments.background_task.grade_all_assignment_task import grade_all_assignment


from assignments.models import AssignmentGrading
from assignments.models.assignment import Assignment
from assignments.models.assignment_transaction import AssignmentTransaction
from users.models import User  # make sure to import the AssignmentGrading model

def automate_grading_service(user, data):
    # from data we receive assignment_id
    if user.role != User.TEACHER:
        return {"error": "Only teachers can automate grading"}, status.HTTP_403_FORBIDDEN

    try:
        assignment = Assignment.objects.get(id=data['as_id'])
    except ObjectDoesNotExist:
        return {"error": "Assignment with given id doesn't exist"}, status.HTTP_400_BAD_REQUEST
    
    subject = assignment.sub_id
    if subject.teacher_id.user != user:
        return {"error": "You are not authorized to automate grading for this subject"}, status.HTTP_403_FORBIDDEN
    
    assignment_transactions = AssignmentTransaction.objects.filter(as_id=assignment)
    if assignment_transactions.count() == 0:
        return {"error": "There is no any assignment submissions"}, status.HTTP_400_BAD_REQUEST

    graded_transactions = assignment_transactions.filter(status="Graded")
    if graded_transactions.count() >0:
        grade_all_assignment.delay(data['as_id'])
        return {"success": "Your auto grading has been initiated "}, status.HTTP_201_CREATED
    else :
        return {"error":"You need to grade 1 subject manually"}, status.HTTP_400_BAD_REQUEST