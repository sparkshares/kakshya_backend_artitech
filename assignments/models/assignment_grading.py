from django.db import models

from assignments.models.assignment_transaction import AssignmentTransaction



class AssignmentGrading(models.Model):
    as_trans_id = models.ForeignKey(AssignmentTransaction, on_delete=models.CASCADE, related_name='assignmentgradings')
    grade = models.CharField(max_length=50)
    remark = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        transaction = AssignmentTransaction.objects.get(id=self.as_trans_id.id)
        transaction.status = "Graded"
        transaction.save()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        transaction = AssignmentTransaction.objects.get(id=self.as_trans_id.id)
        transaction.status = "DeletedGrade"
        transaction.save()
        super().delete(*args, **kwargs)