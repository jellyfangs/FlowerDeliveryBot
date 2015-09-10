# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_user_default_delivery_address'),
        ('order', '0003_auto_20150829_2051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='fulfillment_address',
        ),
        migrations.AddField(
            model_name='deliverygroup',
            name='delivery_time',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_address',
            field=models.ForeignKey(related_name='+', editable=False, to='userprofile.Address', null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_method',
            field=models.CharField(max_length=255, verbose_name='Delivery method', blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping_method',
            field=models.CharField(max_length=255, verbose_name='Shipping method', blank=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='customer_ip_address',
            field=models.GenericIPAddressField(null=True, blank=True),
        ),
    ]
