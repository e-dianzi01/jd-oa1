# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-01 08:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jduser',
            name='u_intg',
            field=models.IntegerField(default=0, verbose_name='用户积分'),
        ),
    ]