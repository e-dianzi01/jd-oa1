# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-26 07:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('goods', '0001_initial'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jdorder',
            name='o_goods',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsDetails', verbose_name='关联商品'),
        ),
        migrations.AddField(
            model_name='jdorder',
            name='o_price',
            field=models.FloatField(default=0, verbose_name='订单总价'),
        ),
        migrations.AddField(
            model_name='jdorder',
            name='o_status',
            field=models.IntegerField(choices=[(0, '待付款'), (1, '待收货'), (2, '待评价')], default=0, verbose_name='订单状态'),
        ),
        migrations.AddField(
            model_name='jdorder',
            name='o_time',
            field=models.DateTimeField(auto_now=True, verbose_name='下单时间'),
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='o_addr',
            field=models.CharField(default='', max_length=255, verbose_name='收货地址'),
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='o_conn',
            field=models.CharField(default='', max_length=20, verbose_name='联系电话'),
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='o_goods',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsDetails', verbose_name='关联商品'),
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='o_price',
            field=models.FloatField(blank=True, null=True, verbose_name='商品价格'),
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='o_status',
            field=models.IntegerField(choices=[(0, '待付款'), (1, '待收货'), (2, '待评价')], default=0, verbose_name='订单状态'),
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='o_time',
            field=models.DateTimeField(auto_now=True, verbose_name='下单时间'),
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='o_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.JdUser', verbose_name='关联用户'),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='o_shopper',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.JdShopper', verbose_name='关联商户'),
        ),
    ]
