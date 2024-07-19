from django.forms import ModelForm, Form
from . models import Professor, Student
from django import forms
class ProfessorForm(ModelForm):
    class Meta:
        model=Professor
        fields= ['username', 'password', 'first_name', 'employee_number','category']
        widgets={
            'password': forms.PasswordInput(),
            'employee_number': forms.NumberInput(),
            'category':forms.Select()
        }

class StudentForm(ModelForm):
    class Meta:
        model=Student
        fields= ['username', 'password', 'first_name', 'enrollment']
        widgets={
            'password': forms.PasswordInput()
        }