# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
        ('destinos_plugin', '0007_auto_20160407_1130'),
    ]

    operations = [
        migrations.AddField(
            model_name='destino',
            name='placeholdercontact',
            field=cms.models.fields.PlaceholderField(null=True, to='cms.Placeholder', slotname='Contacto', editable=False, related_name='contact_placeholder'),
        ),
        migrations.AlterField(
            model_name='destino',
            name='placeholderimgs',
            field=cms.models.fields.PlaceholderField(null=True, to='cms.Placeholder', slotname='Imagenes', editable=False, related_name='images_placeholder'),
        ),
    ]
