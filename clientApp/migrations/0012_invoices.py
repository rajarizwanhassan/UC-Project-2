# Generated by Django 3.1.1 on 2020-09-30 19:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('clientApp', '0011_messagequries_sender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoices',
            fields=[
                ('invoice_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('notes', models.TextField(null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('invoices', models.FileField(upload_to='client_invoices')),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientApp.client')),
            ],
        ),
    ]
