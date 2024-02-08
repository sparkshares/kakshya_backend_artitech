from rest_framework import status

from academics.models.subject_enrolled import SubjectEnrolled
from assignments.models.assignment import Assignment
from assignments.serializers.assignment_serializer import AssignmentSerializer
from django.core.exceptions import ObjectDoesNotExist

def student_assignment_list_service(user):
    try:
        # Fetch the subjects that the student is enrolled in
        enrolled_subjects = SubjectEnrolled.objects.filter(student_id=user.student.id)

        if not enrolled_subjects.exists():
            return {"error": "User is not enrolled in any subjects"}, status.HTTP_400_BAD_REQUEST

        # Fetch the assignments for those subjects
        assignments = Assignment.objects.filter(sub_id__in=[enrollment.sub_id for enrollment in enrolled_subjects])

        if not assignments.exists():
            return {"error": "No assignments found for the subjects the user is enrolled in"}, status.HTTP_404_NOT_FOUND

        # Serialize the assignments
        serializer = AssignmentSerializer(assignments, many=True)

        return serializer.data, status.HTTP_200_OK
    except ObjectDoesNotExist:
        return {"error": "User or subject not found"}, status.HTTP_404_NOT_FOUND
    except Exception as e:
        return {"error": str(e)}, status.HTTP_500_INTERNAL_SERVER_ERROR