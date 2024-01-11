from rest_framework import serializers

from academics.models.subject_material import SubjectMaterial


class SubjectMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectMaterial
        fields = ["id","subm_title","subm_description","sub_filepath","sub_id","updated_at","created_at"]