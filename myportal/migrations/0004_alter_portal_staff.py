# Generated by Django 3.2 on 2021-07-04 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210703_1855'),
        ('myportal', '0003_rename_file_portal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portal',
            name='staff',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
    ]