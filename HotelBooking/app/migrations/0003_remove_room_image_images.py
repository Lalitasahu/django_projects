# Generated by Django 5.1.3 on 2024-12-30 07:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_room_image_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='image',
        ),
        migrations.CreateModel(
            name='images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='rooms/')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.room')),
            ],
        ),
    ]