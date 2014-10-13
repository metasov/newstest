# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='deletednews',
            options={'verbose_name': 'Deleted News', 'verbose_name_plural': 'Deleted News'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ('order',), 'verbose_name': 'News', 'verbose_name_plural': 'News'},
        ),
    ]
