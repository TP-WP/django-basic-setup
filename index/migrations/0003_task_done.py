# Generated by Django 4.1.1 on 2022-10-01 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_rename_proyect_project_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
