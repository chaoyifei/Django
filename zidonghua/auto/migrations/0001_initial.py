# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-06-22 08:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AutoBody',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auto_title', models.CharField(max_length=50)),
                ('auto_body', models.TextField()),
                ('auto_type', models.CharField(max_length=50)),
                ('auto_timestamp', models.DateTimeField()),
                ('auto_imgurl', models.CharField(max_length=50, null=True)),
                ('auto_author', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=20)),
                ('work', models.CharField(max_length=20)),
                ('company', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=20)),
            ],
        ),
    ]
