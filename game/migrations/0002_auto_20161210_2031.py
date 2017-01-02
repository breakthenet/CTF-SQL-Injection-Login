# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HackSession',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('session_id', models.CharField(default=b'', max_length=255, db_index=True)),
                ('tries_left', models.IntegerField(default=100, null=True, blank=True)),
                ('success', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'HackSession',
                'verbose_name_plural': 'HackSessions',
            },
        ),
        migrations.DeleteModel(
            name='Fish',
        ),
    ]
