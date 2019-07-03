# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-02 13:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190702_1951'),
        ('goods', '0006_auto_20190702_1930'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopperImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_img', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsImages', verbose_name='关联商品详细图片')),
                ('m_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.JdShopper', verbose_name='关联商户')),
            ],
            options={
                'verbose_name': '商户表',
                'verbose_name_plural': '商户表',
                'db_table': 'shopper_img',
            },
        ),
        migrations.AlterField(
            model_name='coupon',
            name='user_id',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='用户id'),
        ),
    ]