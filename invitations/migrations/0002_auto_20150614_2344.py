# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invitations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='first_name_normalized',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='guest',
            name='last_name_normalized',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='guest',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='guest',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
    ]
