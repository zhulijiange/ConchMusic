# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-10-18 05:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discover', '0002_auto_20181018_0515'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Friend',
        ),
        migrations.DeleteModel(
            name='MusicFavourite',
        ),
        migrations.DeleteModel(
            name='MusicHistory',
        ),
        migrations.DeleteModel(
            name='MusicList',
        ),
    ]
