# Generated by Django 3.1.7 on 2021-03-10 19:55

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('formulario', '0012_auto_20210310_1402'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FormularioBase',
            new_name='FormularioOMIL',
        ),
    ]