# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-02 11:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_auto_20190701_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsimages',
            name='img_urls',
            field=models.CharField(blank=True, max_length=2000, null=True, verbose_name='商品详情图片'),
        ),
    ]