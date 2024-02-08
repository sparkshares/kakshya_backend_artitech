from rest_framework import serializers
from assignments.models.assignment import Assignment 
from assignments.models.assignment_text import AssignmentText

class AssignmentSerializer(serializers.ModelSerializer):
    assignment_text = serializers.SlugRelatedField(
        source='assignmenttexts', read_only=True, slug_field='text'
    )

    class Meta:
        model = Assignment
        fields = ('id', 'as_title', 'as_description', 'as_filepath', 'sub_id', 'created_at', 'updated_at', 'assignment_text')