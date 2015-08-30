# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_auto_20150812_2343'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='default_delivery_address',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name='default delivery address', blank=True, to='userprofile.Address', null=True),
        ),
    ]
