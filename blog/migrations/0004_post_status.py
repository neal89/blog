# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-30 07:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160826_2230'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]