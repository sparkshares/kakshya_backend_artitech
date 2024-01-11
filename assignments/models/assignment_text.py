from django.db import models

from assignments.models.assignment import Assignment

class AssignmentText(models.Model):
    text = models.TextField()
    a_id = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='assignmenttexts')
    status = models.TextField()
    
    def __str__(self):
        return self.text