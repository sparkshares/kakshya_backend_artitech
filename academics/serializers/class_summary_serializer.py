from rest_framework import serializers
from academics.models.class_record import ClassRecordSummary


class ClassRecordSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRecordSummary
        fields = ["id","summary","record_id","status"]