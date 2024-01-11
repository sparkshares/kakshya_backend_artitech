from django.db import models

from announcement.models.helpers.rename_announcement_material import rename_announcement_material
from users.models.User import Teacher

class Announcement(models.Model):
    ann_title = models.CharField(max_length=200)
    ann_desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teacherannouncements')
    ann_filepath = models.FileField(upload_to=rename_announcement_material)
    