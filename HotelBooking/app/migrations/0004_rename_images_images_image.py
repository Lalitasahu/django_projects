# Generated by Django 5.1.3 on 2024-12-30 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_room_image_images'),
    ]

    operations = [
        migrations.RenameField(
            model_name='images',
            old_name='images',
            new_name='image',
        ),
    ]
