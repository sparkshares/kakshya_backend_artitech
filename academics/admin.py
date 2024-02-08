from django.contrib import admin
from academics.models.class_record import ClassRecord, ClassRecordSummary

from academics.models.subject import Subject
from academics.models.subject_enrolled import SubjectEnrolled
from academics.models.subject_material import SubjectMaterial, SubjectMaterialText

class SubjectAdmin(admin.ModelAdmin):
    list_display = ["id",'sub_title', 'sub_description', 'sub_code', 'teacher_id', 'created_at', 'updated_at']
    
    def get_readonly_fields(self, request, obj=None):
        if obj:  # when editing an object
            return ['sub_code']
        return []

admin.site.register(Subject,SubjectAdmin)
admin.site.register(ClassRecord)
admin.site.register(ClassRecordSummary)
admin.site.register(SubjectMaterial)
admin.site.register(SubjectMaterialText)

admin.site.register(SubjectEnrolled)