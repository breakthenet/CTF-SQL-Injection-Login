# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_delete_hacksession'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthCode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(default=b'', max_length=255)),
                ('name', models.CharField(default=b'', max_length=255)),
                ('last_login', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'AuthCode',
                'verbose_name_plural': 'AuthCodes',
            },
        ),
        migrations.CreateModel(
            name='AuthCodeNum',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.IntegerField(default=0)),
                ('name', models.CharField(default=b'', max_length=255)),
                ('last_login', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'AuthCodeNum',
                'verbose_name_plural': 'AuthCodeNums',
            },
        ),
    ]
