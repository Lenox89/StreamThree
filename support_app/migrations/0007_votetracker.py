# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-11 21:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('support_app', '0006_auto_20190311_2100'),
    ]

    operations = [
        migrations.CreateModel(
            name='VoteTracker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='support_app.Ticket')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
