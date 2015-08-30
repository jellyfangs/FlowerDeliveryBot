# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_prices.models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20150812_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliverygroup',
            name='delivery_price',
            field=django_prices.models.PriceField(decimal_places=4, default=0, editable=False, currency=b'USD', max_digits=12, verbose_name='delivery price'),
        ),
        migrations.AddField(
            model_name='deliverygroup',
            name='delivery_required',
            field=models.BooleanField(default=True, verbose_name='delivery required'),
        ),
        migrations.AddField(
            model_name='order',
            name='fulfillment_address',
            field=models.CharField(max_length=255, verbose_name='Fulfillment method', blank=True),
        ),
        migrations.AlterField(
            model_name='deliverygroup',
            name='status',
            field=models.CharField(default='new', max_length=32, verbose_name='delivery status', choices=[('new', 'Processing'), ('cancelled', 'Cancelled'), ('delivered', 'Delivered'), ('shipped', 'Shipped')]),
        ),
    ]
