# Generated by Django 5.1.3 on 2025-07-03 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='phone',
            new_name='phone_no',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='employee_id',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='is_admin',
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='role',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
