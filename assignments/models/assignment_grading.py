from django.db import models

from assignments.models.assignment_transaction import AssignmentTransaction



class AssignmentGrading(models.Model):
    as_trans_id = models.ForeignKey(AssignmentTransaction, on_delete=models.CASCADE, related_name='assignmentgradings')
    grade = models.CharField(max_length=50)
    remark = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    