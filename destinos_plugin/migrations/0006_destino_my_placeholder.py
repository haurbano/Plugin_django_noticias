# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
        ('destinos_plugin', '0005_auto_20160407_1011'),
    ]

    operations = [
        migrations.AddField(
            model_name='destino',
            name='my_placeholder',
            field=cms.models.fields.PlaceholderField(slotname='Imagenes', to='cms.Placeholder', editable=False, null=True),
        ),
    ]
