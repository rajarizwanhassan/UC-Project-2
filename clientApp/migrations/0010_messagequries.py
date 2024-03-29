# Generated by Django 3.1.1 on 2020-09-27 21:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clientApp', '0009_auto_20200925_2334'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageQuries',
            fields=[
                ('message_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('messageQuery', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('admin_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('client_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clientApp.client')),
                ('operator_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clientApp.operator')),
            ],
        ),
    ]
