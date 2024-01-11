from django.db import models
from academics.models.helper.rename_file import rename_class_record
from academics.models.subject import Subject


class ClassRecord(models.Model):
    class_title = models.CharField(max_length=200)
    class_description= models.TextField()
    audio_path = models.FileField(upload_to=rename_class_record)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    sub_id = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='classrecords')
    
    def __str__(self):
        return self.class_title
    
class ClassRecordSummary(models.Model):
    summary = models.TextField()
    record_id = models.OneToOneField(ClassRecord ,on_delete=models.CASCADE, related_name='classrecordtexts')   
    status = models.TextField()
    
    def __str__(self):
        return self.record_id.class_title