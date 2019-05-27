# Generated by Django 2.2.1 on 2019-05-25 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190525_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='description',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='media',
            name='mgenre',
            field=models.CharField(choices=[('ACT', 'Action'), ('ADV', 'Adventure'), ('DRM', 'Drama'), ('CMDY', 'Comedy'), ('SYFY', 'SyFy')], default='ACT', max_length=20),
        ),
    ]
