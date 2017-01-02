# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_auto_20161210_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='hacksession',
            name='challenge',
            field=models.CharField(default=b'', max_length=255, db_index=True),
        ),
        migrations.AddField(
            model_name='hacksession',
            name='difficulty',
            field=models.IntegerField(default=1, null=True, blank=True),
        ),
    ]
