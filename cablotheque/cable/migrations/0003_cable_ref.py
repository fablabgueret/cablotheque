# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cable', '0002_auto_20150430_2040'),
    ]

    operations = [
        migrations.AddField(
            model_name='cable',
            name='ref',
            field=models.CharField(default=datetime.datetime(2015, 4, 30, 20, 50, 5, 277925, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
