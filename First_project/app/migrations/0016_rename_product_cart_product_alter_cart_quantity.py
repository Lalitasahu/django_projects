# Generated by Django 5.1.3 on 2025-02-06 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='Product',
            new_name='product',
        ),
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
