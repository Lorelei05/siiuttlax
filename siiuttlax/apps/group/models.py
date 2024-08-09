from django.db import models

from apps.periods.models import Semester, Period
from apps.academy.models import Professor, Student
from apps.career.models import Career, Subject

class Group(models.Model):
    group = models.CharField(max_length=1)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    period = models.ForeignKey(Period, on_delete=models.CASCADE)
    tutor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)
    subjects = models.ManyToManyField(Subject)
    career = models.ForeignKey(Career, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.semester} - {self.group} - {self.career}"
