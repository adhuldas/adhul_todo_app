# Generated by Django 3.1.7 on 2021-03-08 04:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='dat',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
