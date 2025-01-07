# Generated by Django 5.1.3 on 2025-01-03 14:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_blogs_datetime_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published'), ('archived', 'Archived')], default='draft', max_length=10),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 3, 14, 50, 49, 94024)),
        ),
    ]
