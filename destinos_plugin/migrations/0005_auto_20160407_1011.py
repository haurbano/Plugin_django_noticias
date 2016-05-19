# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
        ('destinos_plugin', '0004_destinospluginmodel_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destinospluginmodel',
            name='photo',
        ),
        migrations.AddField(
            model_name='destino',
            name='photo',
            field=filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.SET_NULL, help_text='Optional. Image for news article.', null=True, to='filer.Image', blank=True),
        ),
    ]
