# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-01 08:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='author',
            field=models.TextField(default='zihan'),
        ),
        migrations.AlterField(
            model_name='news',
            name='content',
            field=models.TextField(default='test_news'),
        ),
    ]
