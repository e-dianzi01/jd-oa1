# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-26 07:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CollectGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_id', models.IntegerField(verbose_name='用户id')),
                ('g_no', models.IntegerField(verbose_name='商品编号')),
            ],
            options={
                'verbose_name': '收藏商品表',
                'verbose_name_plural': '收藏商品表',
                'db_table': 'collect_goods',
            },
        ),
        migrations.CreateModel(
            name='CollectShopper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_id', models.IntegerField(verbose_name='用户id')),
                ('s_id', models.IntegerField(verbose_name='商户id')),
            ],
            options={
                'verbose_name': '收藏商户表',
                'verbose_name_plural': '收藏商户表',
                'db_table': 'collect_shopper',
            },
        ),
        migrations.CreateModel(
            name='JdShopper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_id', models.CharField(max_length=20, verbose_name='商户ID')),
                ('m_name', models.CharField(max_length=50, verbose_name='商铺名称')),
                ('m_img', models.ImageField(max_length=50, upload_to='', verbose_name='商户图片')),
                ('m_pwd', models.CharField(blank=True, max_length=255, null=True, verbose_name='商家密码')),
                ('m_email', models.CharField(blank=True, max_length=50, null=True, verbose_name='商户邮箱')),
                ('m_phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='手机号')),
                ('s_add', models.CharField(blank=True, max_length=255, null=True, verbose_name='地址')),
                ('is_delete', models.IntegerField(choices=[(0, '未删除'), (1, '已删除')], default=0, verbose_name='删除标志位')),
            ],
            options={
                'verbose_name': '商户表',
                'verbose_name_plural': '商户表',
                'db_table': 'jd_shopper',
            },
        ),
        migrations.CreateModel(
            name='JdUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=50, verbose_name='用户ID')),
                ('user_name', models.CharField(max_length=50, verbose_name='用户名')),
                ('auth_string', models.CharField(max_length=255, verbose_name='用户密码')),
                ('nick_name', models.CharField(max_length=50, null=True, verbose_name='用户昵称')),
                ('is_val', models.IntegerField(choices=[(0, '未验证'), (1, '已验证')], default=0, verbose_name='是否验证')),
                ('tel', models.CharField(max_length=15, null=True, verbose_name='联系电话')),
                ('asset', models.FloatField(default=0, verbose_name='余额')),
                ('u_img', models.ImageField(max_length=255, upload_to='', verbose_name='用户头像')),
                ('u_bank', models.CharField(max_length=50, null=True, verbose_name='银行卡')),
                ('user_card', models.CharField(max_length=50, null=True, verbose_name='身份证号')),
                ('is_login', models.IntegerField(choices=[(0, '未登录'), (1, '已登录')], default=0, verbose_name='是否登录')),
                ('pay_pwd', models.CharField(blank=True, max_length=6, null=True, verbose_name='支付密码')),
            ],
            options={
                'verbose_name': '用户表',
                'verbose_name_plural': '用户表',
                'db_table': 'jd_user',
            },
        ),
        migrations.CreateModel(
            name='LoginUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_name', models.CharField(blank=True, max_length=20, null=True, verbose_name='账号名')),
                ('login_auth_str', models.CharField(blank=True, max_length=200, null=True, verbose_name='密码')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='注册时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_active', models.IntegerField(choices=[(0, '未登录'), (1, '已登录')], default=0, verbose_name='登陆状态')),
                ('note', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name': '管理员表',
                'verbose_name_plural': '管理员表',
                'db_table': 'admins',
            },
        ),
        migrations.CreateModel(
            name='UAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(verbose_name='用户ID')),
                ('user_address', models.CharField(blank=True, max_length=255, null=True, verbose_name='收货地址')),
                ('is_default', models.IntegerField(choices=[(0, '选择'), (1, '不选择')], default=0, verbose_name='默认地址')),
            ],
            options={
                'verbose_name': '地址表',
                'verbose_name_plural': '地址表',
                'db_table': 'u_address',
            },
        ),
        migrations.AddField(
            model_name='jdshopper',
            name='m_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.LoginUser', verbose_name='关联用户'),
        ),
    ]