# Generated by Django 4.2.7 on 2023-11-17 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoVetMartin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pacientes',
            name='fecha_atencion',
            field=models.DateField(),
        ),
    ]
