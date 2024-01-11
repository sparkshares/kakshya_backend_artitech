from django.db import models
from academics.models.helper.rename_file import rename_subject_material
from academics.models.subject import Subject

class SubjectMaterial(models.Model):
    subm_title = models.CharField(max_length=200)
    subm_description = models.TextField()
    sub_filepath = models.FileField(upload_to=rename_subject_material)
    sub_id = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subjectmaterial')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.subm_title

class SubjectMaterialText(models.Model):
    material_text = models.TextField()
    sub_mat_id = models.OneToOneField(SubjectMaterial, on_delete=models.CASCADE, related_name='subjectmaterialtexts')
    status = models.TextField()
    
    def __str__(self):
        return self.sub_mat_id.subm_title

