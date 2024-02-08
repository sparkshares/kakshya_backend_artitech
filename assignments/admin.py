from django.contrib import admin
from assignments.models.assignment import Assignment

from assignments.models.assignment_grading import AssignmentGrading
from assignments.models.assignment_text import AssignmentText
from assignments.models.assignment_transaction import AssignmentTransaction
from assignments.models.assignment_transaction_text import AssignmentTransactionText

# Register your models here.
admin.site.register(AssignmentGrading)
admin.site.register(AssignmentTransaction)
admin.site.register(Assignment)
admin.site.register(AssignmentText)
admin.site.register(AssignmentTransactionText)