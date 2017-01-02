# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20161212_0129'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HackSession',
        ),
    ]
