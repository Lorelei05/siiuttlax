from django.urls import path
from . import views


app_name = 'academy'
urlpatterns = [
    path('student/create',
         views.create_student,
         name='students_create'),
    path('professor/create',
         views.create_prof,
         name='professors_create'),
]
