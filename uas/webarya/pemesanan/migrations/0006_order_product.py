# Generated by Django 5.1.5 on 2025-02-02 11:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aryaapp', '0005_remove_order_customer_remove_order_product_and_more'),
        ('pemesanan', '0005_orderitem_pesan'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='aryaapp.karyaseni'),
        ),
    ]
