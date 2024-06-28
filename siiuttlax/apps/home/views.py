from django.shortcuts import render
from .models import Period, Semester
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    user = request.user
    return render(request, 'home/home.html', {"user": user})

def periods_view(request):
    periods = Period.objects.all()  # Obtener todos los períodos
    return render(request, 'periods.html', {'periods': periods})

def semesters_view(request):
    semesters = Semester.objects.all()  # Obtener todos los semestres
    return render(request, 'semesters.html', {'semesters': semesters})