# Generated by Django 3.1.1 on 2020-10-19 17:57

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clientApp', '0027_auto_20201019_1851'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MessageQuries',
            new_name='MessageQuery',
        ),
    ]
