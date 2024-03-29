# Generated by Django 3.1.1 on 2020-10-11 16:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clientApp', '0022_auto_20201011_1646'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeHoliday',
            fields=[
                ('leave_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('no_of_days', models.IntegerField()),
                ('reason', models.TextField(null=True)),
                ('leave_status', models.CharField(choices=[('Pending', 'Pending'), ('Approve', 'Approve'), ('Decline', 'Decline')], default='Pending', max_length=11)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(null=True)),
                ('read_by_employee', models.BooleanField(default=False)),
                ('read_by_admin', models.BooleanField(default=False)),
                ('admin_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientApp.employee')),
            ],
        ),
    ]
