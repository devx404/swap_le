# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-25 17:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('licenses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='license',
            name='li_institute',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='licensed_institute', to='institutions.Institutions'),
        ),
    ]