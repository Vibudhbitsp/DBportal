# Generated by Django 3.2 on 2021-07-03 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myportal', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='fname',
            new_name='file_name',
        ),
        migrations.AlterField(
            model_name='file',
            name='doc',
            field=models.FileField(blank=True, upload_to='media'),
        ),
    ]
