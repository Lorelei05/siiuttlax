from django.shortcuts import render
from .models import Period, Semester
# Create your views here.
def periods(request):
    periods = Period.objects.all()  # Obtener todos los períodos
    return render(request, 'periods.html', {'periods': periods})

def semesters(request):
    semesters = Semester.objects.all()  # Obtener todos los semestres
    return render(request, 'semesters.html', {'semesters': semesters})