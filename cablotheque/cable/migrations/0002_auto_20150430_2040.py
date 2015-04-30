# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cable', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cable',
            name='photo',
            field=models.ImageField(null=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='cable',
            name='port1',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='cable',
            name='port2',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
