from assignments.background_task.helper.convert_assignment_text import convert_assignment_text
from assignments.models.assignment_transaction import AssignmentTransaction
from assignments.serializers.assignment_transaction_text_serializer import AssignmentTransactionTextSerializer
from celery import shared_task 

@shared_task(bind=True,autoretry_for=(Exception,),retry_backoff=True,max_retries=3)
def create_assignment_transaction_text_task(self, a_id, file_path):
    try:
        assignment_transaction = AssignmentTransaction.objects.get(id=a_id)
    except AssignmentTransaction.DoesNotExist:
        return {"message":"AssignmentTransaction not found"},404

    try:
        # Convert the assignment to text
        text = convert_assignment_text(file_path)

        # Create a new AssignmentText and save it to the database
        assignment_text_data = {
            "text": text,
            "at_id": a_id,
            "status": "completed"  # replace with actual status
        }
        assignment_text_serializer = AssignmentTransactionTextSerializer(data=assignment_text_data)
        if assignment_text_serializer.is_valid():
            assignment_text_serializer.save()
            return {"message": "created successfully"}

        else:
            return {"message": assignment_text_serializer.errors}, 400

    except Exception as e:
        # Handle any exceptions that occur during the conversion process
        return {"message": str(e)}, 500
    
    
    
