# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-05 01:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_auto_20190704_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='vuc',
            field=models.FloatField(blank=True, null=True, verbose_name='价格限制'),
        ),
        migrations.AlterField(
            model_name='goodsdetails',
            name='goods_img',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='商品展示图片地址'),
        ),
        migrations.AlterField(
            model_name='goodsimages',
            name='img_urls',
            field=models.TextField(blank=True, null=True, verbose_name='商品详情图片地址'),
        ),
        migrations.AlterField(
            model_name='shopperimg',
            name='img',
            field=models.TextField(blank=True, null=True, verbose_name='商品详细图片地址'),
        ),
    ]
