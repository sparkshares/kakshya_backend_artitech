from rest_framework import serializers

from assignments.models.assignment_transaction_text import AssignmentTransactionText


class AssignmentTransactionTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentTransactionText
        fields = ["id", "text", "at_id", "status"]