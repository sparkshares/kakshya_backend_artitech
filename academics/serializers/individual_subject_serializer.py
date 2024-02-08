from rest_framework import serializers
from academics.models import Subject, SubjectMaterial, SubjectMaterialText

class SubjectMaterialSerializer(serializers.ModelSerializer):
    sub_material_text = serializers.SlugRelatedField(
        source='subjectmaterialtexts', read_only=True, slug_field='material_text'
    )

    class Meta:
        model = SubjectMaterial
        fields = ["id", "subm_title", "subm_description", "sub_filepath", "sub_id", "created_at", "updated_at", "sub_material_text"]

class IndividualSubjectSerializer(serializers.ModelSerializer):
    subject_materials = SubjectMaterialSerializer(source='subjectmaterial', many=True, read_only=True)

    class Meta:
        model = Subject
        fields = ["id", "sub_title", "sub_description", "sub_code", "teacher_id", "updated_at", "created_at", "subject_materials"]