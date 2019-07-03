# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-02 11:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190701_2102'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collectgoods',
            old_name='lct_id',
            new_name='clt_id',
        ),
        migrations.AddField(
            model_name='jdshopper',
            name='clt',
            field=models.IntegerField(blank=True, null=True, verbose_name='收藏人数'),
        ),
    ]