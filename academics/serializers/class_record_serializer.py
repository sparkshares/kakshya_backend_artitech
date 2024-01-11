from rest_framework import serializers

from academics.models.class_record import ClassRecord


class ClassRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRecord
        fields = ["id", "class_title", "class_description", "audio_path","created_at","updated_at","sub_id"]