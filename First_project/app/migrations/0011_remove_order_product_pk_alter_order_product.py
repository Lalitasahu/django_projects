# Generated by Django 5.1.3 on 2025-05-29 12:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_order_product_pk_alter_order_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product_pk',
        ),
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.product'),
        ),
    ]
