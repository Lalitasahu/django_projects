# Generated by Django 5.1.3 on 2025-07-03 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_rename_phone_profile_phone_no_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='department',
        ),
    ]
