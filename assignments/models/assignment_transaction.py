from django.db import models
from assignments.models.assignment import Assignment
from assignments.models.helper.rename_assignment import rename_assignment_transaction

from users.models.User import Student


class AssignmentTransaction(models.Model):
    as_id = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='assignmenttransactions')
    as_trans_path = models.FileField(upload_to=rename_assignment_transaction)
    submitted_at = models.DateTimeField(auto_now_add=True)
    submitted_by = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='submittedby')
    updated_at = models.DateTimeField(auto_now=True)
    status = models.TextField()
    
    