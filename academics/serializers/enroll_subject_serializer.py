from rest_framework import serializers
from academics.models.subject_enrolled import SubjectEnrolled


class SubjectEnrolledSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectEnrolled
        fields = ["id", "sub_id", "student_id", "status","joined_at"]