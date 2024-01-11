from django.db import models
from academics.models.subject import Subject
from users.models.User import Student

class SubjectEnrolled(models.Model):
    sub_id = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subject_enrolled')
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student')
    status = models.BooleanField(default=True)
    joined_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.sub_id