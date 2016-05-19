# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('destinos_plugin', '0008_auto_20160407_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='destino',
            name='itinerario',
            field=models.TextField(default='itinerario'),
        ),
        migrations.AddField(
            model_name='destino',
            name='numero_contacto',
            field=models.TextField(default='3105555'),
        ),
        migrations.AddField(
            model_name='destino',
            name='valor',
            field=models.TextField(default='0000'),
        ),
        migrations.AlterField(
            model_name='destino',
            name='descripcion',
            field=models.TextField(default='descripcion'),
        ),
        migrations.AlterField(
            model_name='destino',
            name='nombre',
            field=models.TextField(default='Destino'),
        ),
    ]
