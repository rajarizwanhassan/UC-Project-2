# Generated by Django 3.1.1 on 2020-10-06 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientApp', '0014_remove_invoices_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagequries',
            name='read_by_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='messagequries',
            name='read_by_client',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='messagequries',
            name='read_by_operator',
            field=models.BooleanField(default=False),
        ),
    ]
