from django.db import models
from apps.academy.models import Professor
from apps.periods.models import Semester

class Career(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    levels = (
        ('TSU', 'Tecnico Superior Universitario'),
        ('Ing', 'Ingenieria'),
        ('Lic', 'Licenciatura'),
        ('M', 'Maestria')
    )
    director = models.ForeignKey(
        Professor,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Director"
    )
    shortname = models.CharField(max_length=30, blank=False, null=False)
    status = models.BooleanField(default=True)
    level = models.CharField(max_length=3, choices=levels)
    plan = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.level} - {self.shortname}"

    class Meta:
        verbose_name = "carrera"
        verbose_name_plural = "carreras"


class Subject(models.Model):
    name = models.CharField(max_length=100)
    career = models.ForeignKey(Career, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    total_hours = models.IntegerField()
    weekly_hours = models.IntegerField()
    file = models.FileField(
        verbose_name='Archivo',
        blank=True, null=True,
        upload_to='asignaturas/'
    )

    def __str__(self):
        return self.name
