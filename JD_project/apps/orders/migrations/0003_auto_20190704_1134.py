# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-04 03:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
        ('orders', '0002_remove_goodscomment_goods_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodscomment',
            name='goods_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsDetails', verbose_name='关联商品'),
        ),
        migrations.AddField(
            model_name='goodscomment',
            name='order_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='orders.OrderDetail', verbose_name='关联订单'),
        ),
    ]
