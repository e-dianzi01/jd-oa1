# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-01 13:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190701_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectgoods',
            name='lct_id',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='收藏id'),
        ),
        migrations.AlterField(
            model_name='collectgoods',
            name='type_id',
            field=models.IntegerField(blank=True, choices=[(0, '商品'), (1, '商户')], default=0, null=True, verbose_name='商品/商户'),
        ),
        migrations.AlterField(
            model_name='jdshopper',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='注册时间'),
        ),
        migrations.AlterField(
            model_name='jdshopper',
            name='is_active',
            field=models.IntegerField(blank=True, choices=[(0, '未登录'), (1, '已登录')], default=1, null=True, verbose_name='登陆状态'),
        ),
        migrations.AlterField(
            model_name='jdshopper',
            name='is_delete',
            field=models.IntegerField(blank=True, choices=[(0, '未删除'), (1, '已删除')], default=0, null=True, verbose_name='删除标识位'),
        ),
        migrations.AlterField(
            model_name='jdshopper',
            name='is_val',
            field=models.IntegerField(blank=True, choices=[(0, '未验证'), (1, '已验证')], default=1, null=True, verbose_name='验证标识位'),
        ),
        migrations.AlterField(
            model_name='jdshopper',
            name='m_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='商铺名称'),
        ),
        migrations.AlterField(
            model_name='jdshopper',
            name='m_username',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='商主名称'),
        ),
        migrations.AlterField(
            model_name='jdshopper',
            name='update_time',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='jduser',
            name='asset',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='余额'),
        ),
        migrations.AlterField(
            model_name='jduser',
            name='is_delete',
            field=models.IntegerField(blank=True, choices=[(0, '未删除'), (1, '已删除')], default=0, null=True, verbose_name='删除标识位'),
        ),
        migrations.AlterField(
            model_name='jduser',
            name='is_val',
            field=models.IntegerField(blank=True, choices=[(0, '未验证'), (1, '已验证')], default=0, null=True, verbose_name='是否验证'),
        ),
        migrations.AlterField(
            model_name='jduser',
            name='user_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='用户名'),
        ),
    ]