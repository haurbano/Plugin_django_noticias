# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
    ]

    operations = [
        migrations.CreateModel(
            name='DestinosPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, to='cms.CMSPlugin', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(default='Hamilton', max_length=50)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
