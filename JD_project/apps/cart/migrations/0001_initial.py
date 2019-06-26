# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-26 07:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JdCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_goods_num', models.IntegerField(default=1, verbose_name='商品数量')),
                ('freight', models.FloatField(verbose_name='运费')),
                ('c_goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsDetails', verbose_name='关联商品')),
                ('c_shopper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.JdShopper', verbose_name='关联商家')),
                ('c_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.JdUser', verbose_name='关联用户')),
            ],
            options={
                'verbose_name': '商户表',
                'verbose_name_plural': '商户表',
                'db_table': 'jd_cart',
            },
        ),
    ]