# Generated by Django 3.1.7 on 2021-03-12 19:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('formulario', '0013_auto_20210310_1655'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormularioSeguridad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_origen', models.CharField(default='', max_length=30, verbose_name='Pais de Origen')),
                ('tipo_identificacion', models.CharField(choices=[('Rut', 'Rut'), ('Pasaporte', 'Pasaporte'), ('Otro', 'Otro')], default='', max_length=30)),
                ('numero_identificacion', models.CharField(default='', max_length=30)),
                ('nombre', models.CharField(default='', max_length=30, verbose_name='Nombres')),
                ('apellido', models.CharField(default='', max_length=30, verbose_name='Apellidos')),
                ('direccion', models.CharField(default='', max_length=30)),
                ('numero_calle', models.PositiveIntegerField(default=0)),
                ('uv', models.IntegerField(default=0)),
                ('texto1', models.TextField(blank=True, verbose_name='Texto 1')),
                ('texto2', models.TextField(blank=True, verbose_name='Texto 2')),
                ('texto3', models.TextField(blank=True, verbose_name='Texto 3')),
                ('texto4', models.TextField(blank=True, verbose_name='Texto 4')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'formulario base',
                'verbose_name_plural': 'formularios bases',
                'ordering': ['-created'],
            },
        ),
    ]
