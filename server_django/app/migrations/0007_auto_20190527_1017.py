# Generated by Django 2.2.1 on 2019-05-27 10:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20190527_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='date_added',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
