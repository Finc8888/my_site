# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-03 17:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20171103_1837'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('post', models.CharField(max_length=64)),
                ('desc', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Cats',
        ),
    ]
