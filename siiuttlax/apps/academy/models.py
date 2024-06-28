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

    def __str__(self):
        return f"{self.level } - {self.short_name}"

    class Meta:
        verbose_name = 'Profeso r'
        verbose_name_plural = 'Profesores'

class Student(User):
    enrollment = models.CharField(
        max_length=12, 
        verbose_name='Matricula')
    
    def __str__(self):
        return f"{self.level } - {self.short_name}"

    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'

