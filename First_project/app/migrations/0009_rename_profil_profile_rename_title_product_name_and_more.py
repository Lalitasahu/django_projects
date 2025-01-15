# Generated by Django 5.1.3 on 2025-01-13 06:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_category_delete_like'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profil',
            new_name='Profile',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='title',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='images',
            name='user',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.category'),
        ),
    ]
