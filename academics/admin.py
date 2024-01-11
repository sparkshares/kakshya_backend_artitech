from django.contrib import admin
from academics.models.class_record import ClassRecord, ClassRecordSummary

from academics.models.subject import Subject
from academics.models.subject_enrolled import SubjectEnrolled
from academics.models.subject_material import SubjectMaterial, SubjectMaterialText


admin.site.register(Subject)
admin.site.register(ClassRecord)
admin.site.register(ClassRecordSummary)
admin.site.register(SubjectMaterial)
admin.site.register(SubjectMaterialText)

admin.site.register(SubjectEnrolled)