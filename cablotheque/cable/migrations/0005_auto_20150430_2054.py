# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cable', '0004_auto_20150430_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cable',
            name='port1',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cable',
            name='port2',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
