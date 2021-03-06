# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-01 04:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='test_news')),
                ('author', models.TextField(default='test_news')),
                ('content', models.TextField(default='test_content')),
                ('news_url', models.TextField(default='http://', unique=True)),
                ('org_news_date', models.DateTimeField()),
                ('last_modify_date', models.DateTimeField(auto_now=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'news',
            },
        ),
    ]
