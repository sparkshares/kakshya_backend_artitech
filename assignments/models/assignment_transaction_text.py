from django.db import models

from assignments.models.assignment_transaction import AssignmentTransaction


class AssignmentTransactionText(models.Model):
    text = models.TextField()
    at_id = models.ForeignKey(AssignmentTransaction, on_delete=models.CASCADE, related_name='assignmenttransactiontext')
    status = models.TextField()
    
    def __str__(self):
        return str(self.id)