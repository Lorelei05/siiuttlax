from django.urls import path
from . import views

ap_name = 'home'
urlpatterns = [
    path('', views.home, name='home')
]
