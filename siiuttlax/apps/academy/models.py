from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length=100)
    short_name=models.CharField(max_length=15)
    description=models.TextField()
# Create your models here.
class Professor(User):
    employee_number = models.CharField(max_length=4)
    category=models.ForeignKey(
        Category, 
        on_delete=models.CASCADE, 
        default=1)
    title=models.CharField(max_length=100)
class Student(User):
    enrollment = models.CharField(max_length=12, verbose_name='Matrícula')
    


class Principal(User):
    nickname = models.CharField(max_length=50, verbose_name='Usuario')

