# Generated by Django 5.1.3 on 2025-06-04 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_remove_order_product_pk_alter_order_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='laptop_bag',
        ),
        migrations.AddField(
            model_name='order',
            name='cancel_reason',
            field=models.TextField(blank=True, null=True),
        ),
    ]
