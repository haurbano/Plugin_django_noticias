# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('destinos_plugin', '0006_destino_my_placeholder'),
    ]

    operations = [
        migrations.RenameField(
            model_name='destino',
            old_name='photo',
            new_name='photo_inicial',
        ),
        migrations.RenameField(
            model_name='destino',
            old_name='my_placeholder',
            new_name='placeholderimgs',
        ),
    ]
