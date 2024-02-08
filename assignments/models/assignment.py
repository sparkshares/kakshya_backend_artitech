from django.db import models
from academics.models.subject import Subject
from assignments.models.helper.rename_assignment import rename_assignment_material


# Create your models here.
class Assignment(models.Model):
    as_title = models.CharField(max_length=200)
    as_description = models.TextField()
    as_filepath = models.FileField(upload_to=rename_assignment_material)
    sub_id = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='assignments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.id)