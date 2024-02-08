from assignments.background_task.helper.gpt_grade_assignment import gpt_grade_assignment
from assignments.models.assignment_grading import AssignmentGrading
from assignments.models.assignment_text import AssignmentText
from assignments.models.assignment_transaction import AssignmentTransaction
from assignments.models.assignment_transaction_text import AssignmentTransactionText
from celery import shared_task
from django.core.exceptions import ObjectDoesNotExist
from openai import OpenAI
import os

api_key = os.getenv('OPENAI_API_KEY')

@shared_task(bind=True, autoretry_for=(Exception,), retry_backoff=True, max_retries=3)
def grade_all_assignment(self, a_id):
    
    client = OpenAI(api_key=api_key)

    try:
        # Get a random AssignmentTransaction related to the Assignment with status "Graded"
        transaction = AssignmentTransaction.objects.filter(as_id=a_id, status="Graded").order_by('?').first()
    except ObjectDoesNotExist:
        return {"error": "No graded AssignmentTransaction found for this Assignment"}
    try:
        # Get the AssignmentGrading related to the AssignmentTransaction
        grading = AssignmentGrading.objects.get(as_trans_id=transaction.id)
    except ObjectDoesNotExist:
        return {"error": "No AssignmentGrading found for this AssignmentTransaction transaction id = "+str(transaction.id)+" a_id = "+str(a_id)}

    grade_detail = grading.grade
    remark = grading.remark

    try:
        # Get the AssignmentTransactionText related to the AssignmentTransaction
        transaction_text = AssignmentTransactionText.objects.get(at_id=transaction.id)
    except ObjectDoesNotExist:
        return {"error": "No AssignmentTransactionText found for this AssignmentTransaction"}


    try:
        # Store the AssignmentText value in a variable
        assignment_text = AssignmentText.objects.get(a_id=transaction.as_id.id).text
    
    except ObjectDoesNotExist:
        return {"error": "No AssignmentText found for this Assignment, assignment id is ="+str(transaction.as_id.id)}

    assignment_transactions = AssignmentTransaction.objects.filter(as_id=a_id).exclude(status="Graded")
    
    if not assignment_transactions.exists():
        return {"error": "No data found for the given a_id"}
    
    transaction_details = []

    for transaction in assignment_transactions:
        try:
            transaction_text = AssignmentTransactionText.objects.get(at_id=transaction.id).text
            transaction_details.append({"transaction_id": transaction.id, "transaction_text": transaction_text})
        except ObjectDoesNotExist:
            print({"error":"No AssignmentTransactionText found for AssignmentTransaction with id {transaction.id}"})
            continue
        
        gpt_grade_assignment(assignment_text,transaction_text,grade_detail,remark,transaction.id,transaction_text)
