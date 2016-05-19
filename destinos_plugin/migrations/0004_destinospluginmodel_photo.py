# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
        ('destinos_plugin', '0003_destino'),
    ]

    operations = [
        migrations.AddField(
            model_name='destinospluginmodel',
            name='photo',
            field=filer.fields.image.FilerImageField(to='filer.Image', help_text='Optional. Image for news article.', null=True, blank=True, on_delete=django.db.models.deletion.SET_NULL),
        ),
    ]
