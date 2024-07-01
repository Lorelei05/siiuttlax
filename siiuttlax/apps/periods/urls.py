from django.urls import path
from . import views


app_name = 'periods'
urlpatterns = [
    path('', views.periods, name='periods'),
]

app_name = 'semesters'
urlpatterns = [
    path('', views.semesters, name='semesters'),
]
