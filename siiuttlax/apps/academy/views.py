from django.shortcuts import render, redirect
from .forms import ProfessorForm, StudentForm
from .models import Professor, Student

def create_prof(request):
    if request.method == 'POST':
        form=ProfessorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('academy:professors_create')

    form=ProfessorForm()
    return render(request,
                'academy/create_professor.html',   
                {'form':form})
  
  
def create_student(request):
    if request.method == 'POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('academy:students_create')
    form=StudentForm()
    return render(request,
                'academy/create_student.html',
                {'form':form})

