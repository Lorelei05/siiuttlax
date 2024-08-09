from django.contrib import admin
from .models import Career, Subject

@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ['shortname', 'level', 'name']
    ordering = ['level', 'shortname']


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'career', 'semester', 'total_hours', 'weekly_hours', 'file']
    list_filter = ['career', 'semester']
