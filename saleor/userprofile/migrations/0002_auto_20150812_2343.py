# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.CharField(blank=True, max_length=2, verbose_name='country', choices=[('US', 'United States'), ('CA', 'Canada')]),
        ),
        migrations.AlterField(
            model_name='address',
            name='phone',
            field=models.CharField(max_length=30, verbose_name='phone number'),
        ),
    ]
