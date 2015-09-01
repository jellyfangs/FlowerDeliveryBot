# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20150829_2340'),
    ]

    operations = [
        migrations.AddField(
            model_name='productvariant',
            name='is_stocking_required',
            field=models.BooleanField(default=False),
        ),
    ]
