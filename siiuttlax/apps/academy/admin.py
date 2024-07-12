from django.contrib import admin
from .models import Professor, Student, Category
# Register your models here.
admin.site.register(Category)

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'category', 'employee_number', 'title')
    fields=('first_name', 'username','last_name','category','employee_number', 'title', 'email')
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ( 'first_name','username', 'last_name', 'enrollment')
    fields=('first_name','username', 'last_name','enrollment','email')