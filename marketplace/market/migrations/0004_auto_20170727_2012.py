# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 12:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='types_place',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='username',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='usertype',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
