# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-11 16:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_auto_20171111_1716'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Logo',
        ),
        migrations.AddField(
            model_name='hobby',
            name='image',
            field=models.ImageField(null=True, upload_to='logo'),
        ),
    ]
