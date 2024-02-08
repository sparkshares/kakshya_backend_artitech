from rest_framework import serializers
from academics.models.subject import Subject
from assignments.models.assignment_transaction import AssignmentTransaction
from academics.models.subject_enrolled import SubjectEnrolled

class AssignmentTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentTransaction
        fields = ["id","as_id","as_trans_path","submitted_at","submitted_by","updated_at","status"]

    def validate(self, data):
        assignment = data['as_id']
        student = data['submitted_by']
        subject = assignment.sub_id

        if not SubjectEnrolled.objects.filter(sub_id=subject, student_id=student).exists():
            raise serializers.ValidationError("The student is not enrolled in this subject")

        return data