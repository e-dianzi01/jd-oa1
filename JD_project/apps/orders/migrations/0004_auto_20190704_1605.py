# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-04 08:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20190704_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='o_num',
            field=models.CharField(max_length=255, primary_key=True, serialize=False, verbose_name='订单号'),
        ),
    ]