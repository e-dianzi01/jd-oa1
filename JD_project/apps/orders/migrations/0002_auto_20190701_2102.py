# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-01 13:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='g_id',
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='o_addr',
            field=models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='收货地址'),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='o_conn',
            field=models.CharField(blank=True, default='', max_length=20, null=True, verbose_name='联系电话'),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='o_status',
            field=models.IntegerField(blank=True, choices=[(0, '待付款'), (1, '待收货'), (2, '待评价')], default=0, null=True, verbose_name='订单状态'),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='o_time',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='下单时间'),
        ),
    ]