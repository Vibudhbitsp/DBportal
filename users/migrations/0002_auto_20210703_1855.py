# Generated by Django 3.2 on 2021-07-03 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='city_circle',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='qualifier',
        ),
    ]