# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-11 14:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_auto_20171111_1639'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work',
            name='name',
        ),
        migrations.AddField(
            model_name='work',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.Organization', verbose_name='Организация'),
        ),
        migrations.AddField(
            model_name='work',
            name='period',
            field=models.PositiveIntegerField(default=1, verbose_name='Время работы'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.CharField(max_length=32, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='region',
            field=models.CharField(max_length=32, verbose_name='Регион'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='site',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Сайт'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='tax_id',
            field=models.PositiveIntegerField(null=True, verbose_name='ИНН'),
        ),
        migrations.AlterField(
            model_name='work',
            name='desc',
            field=models.TextField(blank=True, null=True, verbose_name='Обязанности'),
        ),
        migrations.AlterField(
            model_name='work',
            name='post',
            field=models.CharField(max_length=64, verbose_name='Должность'),
        ),
    ]
