# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('destinos_plugin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destinospluginmodel',
            name='user_name',
            field=models.CharField(max_length=200, default='Hamilton'),
        ),
    ]
