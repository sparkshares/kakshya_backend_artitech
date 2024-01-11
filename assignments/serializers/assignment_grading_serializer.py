from rest_framework import serializers

from assignments.models import assignment_grading

class AssingmentGradingSerializer(serializers.ModelSerializer):
    class Meta:
        model = assignment_grading
        fields = ["id","as_trans_id","grade","remark","created_at","updated_at"]
        
