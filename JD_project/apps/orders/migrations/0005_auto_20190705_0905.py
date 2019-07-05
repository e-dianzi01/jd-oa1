# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-05 01:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20190704_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='o_status',
            field=models.IntegerField(blank=True, choices=[(0, '待付款'), (1, '待收货'), (2, '待评价'), (3, '已失效')], default=0, null=True, verbose_name='订单状态'),
        ),
    ]
