from django.urls import path
from assignments.views.submit_assignment_view import submit_assignment_view

from assignments.views.create_assignment import create_assignment_view

urlpatterns = [
    path('create/',create_assignment_view,name="create_assignment"),
    path('submit-assignment',submit_assignment_view,name="submit_assignment")
]