from assignments.background_task.helper.convert_assignment_text import convert_assignment_text
from assignments.models.assignment import Assignment
from assignments.serializers.assignment_text_serializer import AssignmentTextSerializer
from celery import shared_task 

@shared_task(bind=True,autoretry_for=(Exception,),retry_backoff=True,max_retries=3)
def create_assignment_text_task(self, a_id, file_path):
    try:
        assignment= Assignment.objects.get(id=a_id)
    except Assignment.DoesNotExist:
        return {"message":"Assignment not found"},404

    try:
        # Convert the assignment to text
        text = convert_assignment_text(file_path)

        # Create a new AssignmentText and save it to the database
        assignment_text_data = {
            "text": text,
            "a_id": a_id,
            "status": "completed"  # replace with actual status
        }
        
        assignment_text_serializer = AssignmentTextSerializer(data=assignment_text_data)
        if assignment_text_serializer.is_valid():
            assignment_text_serializer.save()
            return {"message": "created successfully"}

        else:
            return {"message": assignment_text_serializer.errors}, 400

    except Exception as e:
        # Handle any exceptions that occur during the conversion process
        return {"message": str(e)}, 500