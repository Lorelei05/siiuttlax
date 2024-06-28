from django.contrib import admin
from .models import Professor, Student, Category
# Register your models here.
admin.site.register(Category)
admin.site.register(Professor)
admin.site.register(Student)