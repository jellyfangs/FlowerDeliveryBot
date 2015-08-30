# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20150812_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='productvariant',
            name='is_delivery_required',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='productvariant',
            name='is_shipping_required',
            field=models.BooleanField(default=False),
        ),
    ]
