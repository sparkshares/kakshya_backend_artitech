from rest_framework import serializers

from assignments.models.assignment_grading import AssignmentGrading


class AssignmentGradingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentGrading
        fields = ["id","as_trans_id","grade","remark","created_at","updated_at"]
        
