# Generated by Django 5.1.3 on 2024-12-09 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Room_no', models.IntegerField()),
                ('Room_type', models.CharField(choices=[('Single', 'Single'), ('Double', 'Double'), ('Suite', 'Suite')], max_length=10)),
                ('AC_Room', models.CharField(max_length=10)),
                ('Non_AC_Room', models.CharField(max_length=10)),
                ('Price_per_night', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Room_available', models.BooleanField(default=True)),
                ('Room_description', models.TextField(blank=True)),
            ],
        ),
    ]
