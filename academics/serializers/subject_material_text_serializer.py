from rest_framework import serializers

from academics.models.subject_material import SubjectMaterialText


class SubjectMaterialTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectMaterialText
        fields = ["id", "material_text", "sub_mat_id", "status"]