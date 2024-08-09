from django.contrib import admin

# Register your models here.
from .models import Semester, Period

@admin.register(Period)
class PeriodAdmin(admin.ModelAdmin):
    list_display = ['year','period','cicle','is_active']
    list_editable = ['is_active']
    
@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ['semester_name']
    