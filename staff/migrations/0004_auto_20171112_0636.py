# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-12 14:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0003_auto_20171005_0103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='deleted',
            field=models.CharField(default='N', max_length=1),
        ),
    ]
