# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('length', models.IntegerField()),
                ('port1', models.CharField(max_length=200)),
                ('port2', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to=b'')),
            ],
        ),
    ]
