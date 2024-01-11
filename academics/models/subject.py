import random
import string
from django.db import models
from users.models import Teacher


class Subject(models.Model):
    sub_title = models.CharField(max_length=200)
    sub_description = models.TextField()
    sub_code = models.CharField(max_length=200, blank=True, editable=False)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teacher')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.sub_code:
            self.sub_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.sub_title
    
