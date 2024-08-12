from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    user = request.user
    try:
        if user.professor:
            #type_user = 'professor'
            return redirect('home:professor')
    except:
        type_user = 'other'
    
    if type_user == 'other':
        try:
            #if user.student:type_user = 'student'
            return redirect('home:student')
        except: type_user = 'other'

    context = {
        "user": user,
        "type_user": type_user
    }
    return render(request, 'home/home.html', context)

def student(request):
    user = request.user
    student = user.student
    group = student.group_set.all().first()
    
    if group is not None:
        career = group.career
    else:
        career = None 

    context = {
        'student': student,
        'group': group,
        'career': career
    }
    return render(request, 'home/student.html', context)


def professor(request):
    user = request.user
    professor = user.professor
    group = professor.group_set.all().first()
    if group is not None:
        career = group.career
    else:
        career = None 


    context = {
        'professor': professor,
        'group': group,
        'career': career
    }
    return render(request, 'home/professor.html', context)