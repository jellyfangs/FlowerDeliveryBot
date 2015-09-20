# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20150825_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='due',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 20, 5, 4, 31, 245371, tzinfo=utc), verbose_name='due'),
            preserve_default=False,
        ),
    ]
