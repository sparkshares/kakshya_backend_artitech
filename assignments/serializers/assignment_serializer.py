from rest_framework import serializers
from assignments.models.assignment import Assignment 

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ('id', 'as_title', 'as_description', 'as_filepath', 'sub_id', 'created_at', 'updated_at')