# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-06-30 02:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0003_auto_20170627_1124'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AutoBody',
        ),
        migrations.DeleteModel(
            name='UserInfo',
        ),
    ]
