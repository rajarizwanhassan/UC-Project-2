# Generated by Django 3.1 on 2020-09-16 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientApp', '0006_leave_reason'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='admin_leave_status',
            field=models.CharField(default='Pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='leave',
            name='client_leave_status',
            field=models.CharField(default='Pending', max_length=20),
        ),
    ]