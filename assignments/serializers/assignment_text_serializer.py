from rest_framework import serializers
from assignments.models.assignment_text import AssignmentText
from assignments.models.assignment import Assignment  # Import the Assignment model

class AssignmentTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentText
        fields = ["id", "text", "a_id", "status"]