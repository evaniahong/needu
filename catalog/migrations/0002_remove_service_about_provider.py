# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-09-20 22:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='about_provider',
        ),
    ]