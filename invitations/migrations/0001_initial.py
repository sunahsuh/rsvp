# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import invitations.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('rsvp', models.NullBooleanField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(default=invitations.models.get_key, max_length=32)),
                ('hashtag_suggestion', models.CharField(max_length=255, blank=True)),
                ('song_suggestions', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='guest',
            name='invitation',
            field=models.ForeignKey(to='invitations.Invitation'),
        ),
    ]
