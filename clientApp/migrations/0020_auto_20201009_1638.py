# Generated by Django 3.1.1 on 2020-10-09 15:38

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clientApp', '0019_empyloyee'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Empyloyee',
            new_name='Employee',
        ),
    ]