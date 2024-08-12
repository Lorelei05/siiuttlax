from . models import Professor, Student
from django.contrib.auth.forms import UserCreationForm
class ProfessorForm(UserCreationForm):
    class Meta:
        model=Professor
        fields= ['username', 'password', 'first_name', 'employee_number',
                'category', 'password1', 'password2']

class StudentForm(UserCreationForm):
    class Meta:
        model=Student
        fields= ['username', 'password', 'first_name', 'enrollment',
                'password1', 'password2']