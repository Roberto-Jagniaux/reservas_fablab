# Generated by Django 4.1 on 2023-12-19 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloque', '0009_remove_reserva_ide'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='idB',
        ),
        migrations.AddField(
            model_name='reserva',
            name='idE',
            field=models.ManyToManyField(to='bloque.stock'),
        ),
    ]
