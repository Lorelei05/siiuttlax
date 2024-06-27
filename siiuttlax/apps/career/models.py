from django.db import models

class Career(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    levels = (
        ('TSU', 'Tecnico Superior Universitario'),
        ('Ing', 'Ingenieria'),
        ('Lic', 'Licenciatura'),
        ('M', 'Maestria')
    )
    shortname = models.CharField(max_length=30, blank=False, null=False)
    status = models.BooleanField(default=True)
    level = models.CharField(max_length=3, choices=levels)
    plan = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100)
    career = models.ForeignKey(Career, on_delete=models.CASCADE)
    semester = models.IntegerField()
    weekly_hours = models.IntegerField()
    file = models.CharField(max_length=100)

    def __str__(self):
        return self.name
