# Generated by Django 3.1 on 2020-08-30 14:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('client_user_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('client_name', models.CharField(max_length=100)),
                ('client_type', models.CharField(choices=[('', 'Choose...'), ('Taxi Firm', 'Taxi Firm'), ('Insurance Firm', 'Insurance Firm'), ('Others', 'Others')], max_length=30)),
                ('contact_number', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
                ('address', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='client_profile_picture')),
                ('user_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('operator_user_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('operator_name', models.CharField(max_length=100)),
                ('contact_number', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
                ('address', models.CharField(max_length=200)),
                ('total_leaves', models.IntegerField()),
                ('avaliable_leaves', models.IntegerField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='operator_profile_picture')),
                ('client_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clientApp.client')),
                ('user_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('leave_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('no_of_days', models.CharField(choices=[('', 'Choose...'), ('One', 'One'), ('Two', 'Two'), ('Three', 'Three'), ('Four', 'Four'), ('Five', 'Five'), ('More', 'More')], max_length=20)),
                ('leave_status', models.CharField(choices=[('Pending', 'Pending'), ('Approve', 'Approve'), ('Decline', 'Decline')], default='Pending', max_length=20)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(null=True)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientApp.client')),
                ('operator_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientApp.operator')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('feedback_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('rating', models.CharField(choices=[('', 'Choose...'), ('One Star', 'One Star'), ('Two Star', 'Two Star'), ('Three Star', 'Three Star'), ('Four Star', 'Four Star'), ('Five Star', 'Five Star')], max_length=20)),
                ('feedback_note', models.TextField()),
                ('client_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clientApp.client')),
                ('operator_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientApp.operator')),
            ],
        ),
    ]
