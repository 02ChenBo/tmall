# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-06-08 07:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20180608_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopcar',
            name='car_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
