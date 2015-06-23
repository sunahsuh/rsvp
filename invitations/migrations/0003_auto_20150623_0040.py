# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invitations', '0002_auto_20150614_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='hashtag_suggestion',
            field=models.CharField(max_length=255, verbose_name=b'Wedding Hashtag Suggestion', blank=True),
        ),
    ]
