# Generated by Django 3.2 on 2021-07-07 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_profile_user'),
        ('myportal', '0006_alter_portal_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portal',
            name='staff',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
    ]