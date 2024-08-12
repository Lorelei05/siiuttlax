
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('academy', '0001_initial'),
        ('periods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('shortname', models.CharField(max_length=30)),
                ('status', models.BooleanField(default=True)),
                ('level', models.CharField(choices=[('TSU', 'Tecnico Superior Universitario'), ('Ing', 'Ingenieria'), ('Lic', 'Licenciatura'), ('M', 'Maestria')], max_length=3)),
                ('plan', models.DateTimeField(auto_now_add=True)),
                ('director', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='academy.professor', verbose_name='Director')),
            ],
            options={
                'verbose_name': 'carrera',
                'verbose_name_plural': 'carreras',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('total_hours', models.IntegerField()),
                ('weekly_hours', models.IntegerField()),
                ('file', models.FileField(blank=True, null=True, upload_to='asignaturas/', verbose_name='Archivo')),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='career.career')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='periods.semester')),
            ],
        ),
    ]
