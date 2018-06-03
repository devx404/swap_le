# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-05-27 11:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('institutions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('li_key', models.CharField(max_length=45)),
                ('li_expiration_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('li_created', models.DateTimeField(auto_now_add=True)),
                ('li_updated', models.DateTimeField(auto_now=True)),
                ('li_max_staff', models.IntegerField(default=0)),
                ('li_max_students', models.IntegerField(default=0)),
                ('li_max_assesments', models.IntegerField(default=0)),
                ('li_current_staff', models.IntegerField(default=0)),
                ('li_current_students', models.IntegerField(default=0)),
                ('li_current_assesments', models.IntegerField(default=0)),
                ('li_current_status', models.CharField(choices=[(b'inac', b'Inactive'), (b'acti', b'Active'), (b'expi', b'Expired')], default=b'inac', max_length=4)),
                ('li_institute', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='licensed_institute', to='institutions.Institutions')),
            ],
            options={
                'ordering': ('-li_current_assesments',),
            },
        ),
    ]