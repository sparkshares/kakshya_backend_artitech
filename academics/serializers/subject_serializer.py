from rest_framework import serializers
from academics.models import Subject

class SubjectSerializer(serializers.ModelSerializer):
    
        class Meta:
            model = Subject
            fields = ["id", "sub_title", "sub_description", "sub_code","teacher_id","updated_at","created_at"]