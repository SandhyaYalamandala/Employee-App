# Generated by Django 4.0.4 on 2022-05-06 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_alter_employee_edesignation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='edesignation',
            field=models.CharField(max_length=200),
        ),
    ]
