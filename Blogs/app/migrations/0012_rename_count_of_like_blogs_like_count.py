# Generated by Django 5.1.3 on 2025-01-08 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_likes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogs',
            old_name='count_of_Like',
            new_name='like_count',
        ),
    ]
