# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-11 19:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='votes',
            field=models.IntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='description',
            field=models.TextField(verbose_name='Describe the issue:'),
        ),
    ]
