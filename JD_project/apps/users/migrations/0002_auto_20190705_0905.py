# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-05 01:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shoppertype',
            options={'verbose_name': '商户分类', 'verbose_name_plural': '商户分类'},
        ),
        migrations.AlterField(
            model_name='jdshopper',
            name='m_img',
            field=models.ImageField(blank=True, default='qw.jpg', null=True, upload_to='users/photo', verbose_name='商户图片地址'),
        ),
        migrations.AlterField(
            model_name='jduser',
            name='u_img',
            field=models.ImageField(blank=True, default='qw.jpg', null=True, upload_to='users/photo', verbose_name='用户头像'),
        ),
        migrations.AlterField(
            model_name='uaddress',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.JdUser', verbose_name='关联用户'),
        ),
    ]
