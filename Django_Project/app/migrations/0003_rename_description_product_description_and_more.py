# Generated by Django 5.1.3 on 2024-11-22 07:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_product_is_deleted_alter_product_posted_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Title',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='product',
            name='Posted_date',
        ),
        migrations.AddField(
            model_name='product',
            name='posted_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]