# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DeletedNews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=120, verbose_name=b'Title')),
                ('description', models.TextField(verbose_name=b'Description')),
                ('creation_date', models.DateField(default=datetime.date.today, verbose_name=b'Creation Date')),
                ('publication_date', models.DateField(default=datetime.date.today, verbose_name=b'Publication Date')),
                ('order', models.IntegerField(default=1, verbose_name=b'Order')),
            ],
            options={
                'ordering': ('order',),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='deletednews',
            name='news',
            field=models.ForeignKey(related_name=b'users_deleted', to='news.News'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='deletednews',
            name='user',
            field=models.ForeignKey(related_name=b'deleted_news', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
