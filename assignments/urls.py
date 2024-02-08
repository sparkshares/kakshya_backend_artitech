from django.urls import path
from assignments.views.student_assignment_list_view import student_assignment_list_view
from assignments.views.automate_grading_view import automate_grading_view
from assignments.views.grade_assignment_view import grade_assignment_view
from assignments.views.submit_assignment_view import submit_assignment_view

from assignments.views.create_assignment import create_assignment_view

urlpatterns = [
    path('create/',create_assignment_view,name="create_assignment"),
    path('submit-assignment',submit_assignment_view,name="submit_assignment"),
    path('grade-assignment',grade_assignment_view,name="grade_assignment"),
    path('automate-grading',automate_grading_view,name="automate_grading"),
    path('student-assignment-list',student_assignment_list_view,name='student_assignment_list')
]