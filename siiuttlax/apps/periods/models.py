from django.db import models

# Create your models here.
class Period(models.Model):
    PERIODS = [
        ('enero - abril', 'enero - abril'),
        ('mayo -  agosto', 'mayo - agosto'),
        ('septiembre - diciembre', 'septiembre - diciembre')
    ]
    period = models.CharField(max_length=25, choices=PERIODS, verbose_name='Periodo')
    year = models.CharField(max_length=4, verbose_name='Año', default=2024)
    cycle = models.CharField(max_length=15, verbose_name='Ciclo', default='2024 - 2025')
    year = models.CharField(max_length=4,verbose_name='Año', default=2024)
    cicle = models.CharField(max_length=15, verbose_name='Ciclo', default='2024 - 2025')
    is_active =models.BooleanField(verbose_name='Activo', default=False)

    def _str_(self):

        return f'{ self.period } { self.year }'
    class Meta:
        verbose_name = 'Periodo'
        verbose_name_plural = 'Periodos'
        ordering=['id']

class  Semester(models.Model):
    semester = models.CharField(max_length=10, verbose_name="Cuatrimestre")

    semester_name = models.CharField(max_length=10, verbose_name="Cuatrimestre en Letra")

    def _str_(self):

        return f'{self.semester_name}'
    
    class Meta:
        verbose_name = 'Cuatrimestre'
        verbose_name_plural = 'Cuatrimestres'
        ordering=['id']