from django.urls import path
from academics.views.create_class_record import create_class_record_view
from academics.views.create_subject_material import create_subject_material_view
from academics.views.enroll_subject import enroll_subject_view

from academics.views.subject import create_subject_view, list_subject_view

urlpatterns = [
    path('subjects/create/',create_subject_view,name="create-subject" ),
    path('subjects/',list_subject_view,name="list-subject"),
    path('enroll/',enroll_subject_view,name="enroll-subject"),
    path('subjects/create-study-material/',create_subject_material_view,name='create-subject-material'),
    path('subjects/create-class-record/',create_class_record_view,name='create-class-record')
]