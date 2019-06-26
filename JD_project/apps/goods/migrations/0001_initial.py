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
            name='GoodsComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_id', models.IntegerField(verbose_name='商品id')),
                ('user_id', models.IntegerField(verbose_name='用户id')),
                ('order_id', models.IntegerField(verbose_name='订单id')),
                ('m_id', models.IntegerField(verbose_name='店铺id')),
                ('grade', models.IntegerField(default=4, verbose_name='评分')),
                ('comment_content', models.CharField(default='东西强烈好评', max_length=255, verbose_name='评论内容')),
                ('comment_time', models.DateTimeField(auto_now_add=True, verbose_name='评论时间')),
            ],
            options={
                'verbose_name': '商品评论表',
                'verbose_name_plural': '商品评论表',
                'db_table': 'goods_comment',
            },
        ),
        migrations.CreateModel(
            name='GoodsDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_id', models.IntegerField(verbose_name='店铺id')),
                ('good_img', models.CharField(max_length=255, null=True, verbose_name='商品展示图片')),
                ('goods_name', models.CharField(max_length=200, verbose_name='商品名称')),
                ('goods_prices', models.FloatField(default=0, max_length=50, verbose_name='商品单价')),
                ('kill_prices', models.FloatField(default=0, max_length=50, verbose_name='秒杀价格')),
                ('goods_num', models.IntegerField(default=1, verbose_name='商品库存')),
                ('goods_state', models.IntegerField(choices=[(0, '上架'), (1, '下架')], default=0, verbose_name='商品上架状态')),
                ('one_category_id', models.IntegerField(verbose_name='一级分类id')),
                ('two_category_id', models.IntegerField(verbose_name='二级分类id')),
                ('goods_no', models.CharField(max_length=50, verbose_name='商品编号')),
                ('keywords', models.CharField(max_length=50, verbose_name='关键字')),
                ('remark', models.CharField(max_length=255, null=True, verbose_name='备注')),
            ],
            options={
                'verbose_name': '商品详细表',
                'verbose_name_plural': '商品详细表',
                'db_table': 'goods_details',
            },
        ),
        migrations.CreateModel(
            name='GoodsImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_id', models.IntegerField(verbose_name='商品id')),
                ('img_urls', models.CharField(max_length=255, verbose_name='商品详情图片')),
            ],
            options={
                'verbose_name': '商品图片表',
                'verbose_name_plural': '商品图片表',
                'db_table': 'goods_imgs',
            },
        ),
        migrations.CreateModel(
            name='GoodsRec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_name', models.CharField(max_length=30, verbose_name='页面名称')),
                ('img_urls', models.CharField(max_length=200, verbose_name='图片链接')),
                ('remark', models.CharField(max_length=50, verbose_name='备注')),
            ],
            options={
                'verbose_name': '商品推荐表',
                'verbose_name_plural': '商品推荐表',
                'db_table': 'goods_rec',
            },
        ),
        migrations.CreateModel(
            name='GoodsSeckill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_name', models.CharField(max_length=30, verbose_name='页面名称')),
                ('page_text', models.CharField(max_length=100, null=True, verbose_name='文字内容')),
                ('kill_time', models.DateTimeField(auto_now_add=True, verbose_name='秒杀时间')),
                ('remark', models.CharField(max_length=50, null=True, verbose_name='备注')),
                ('goods_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsDetails')),
            ],
            options={
                'verbose_name': '秒杀表',
                'verbose_name_plural': '秒杀表',
                'db_table': 'goods_seckill',
            },
        ),
        migrations.CreateModel(
            name='GoodsSku',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_id', models.IntegerField(verbose_name='商品id')),
                ('goods_num', models.IntegerField(default=1, verbose_name='商品库存')),
                ('properties', models.CharField(max_length=50, null=True, verbose_name='属性')),
            ],
            options={
                'verbose_name': '商品属性规格表',
                'verbose_name_plural': '商品属性规格表',
                'db_table': 'goods_sku',
            },
        ),
        migrations.CreateModel(
            name='GoodsType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_id', models.IntegerField(verbose_name='商品id')),
                ('one_type_name', models.CharField(max_length=20, null=True, verbose_name='一级分类名称')),
                ('two_type_name', models.CharField(max_length=20, null=True, verbose_name='二级分类名称')),
                ('remark', models.CharField(max_length=50, null=True, verbose_name='备注')),
            ],
            options={
                'verbose_name': '商品分类表',
                'verbose_name_plural': '商品分类表',
                'db_table': 'goods_type',
            },
        ),
        migrations.CreateModel(
            name='Nav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_name', models.CharField(max_length=30, verbose_name='页面名称')),
                ('img_urls', models.CharField(max_length=200, verbose_name='图片链接')),
                ('remark', models.CharField(max_length=50, verbose_name='备注')),
                ('page_text', models.CharField(max_length=100, null=True, verbose_name='文字内容')),
            ],
            options={
                'verbose_name': '导航表',
                'verbose_name_plural': '导航表',
                'db_table': 'nav',
            },
        ),
        migrations.CreateModel(
            name='SlideShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_name', models.CharField(max_length=30, verbose_name='页面名称')),
                ('img_urls', models.CharField(max_length=200, verbose_name='图片链接')),
                ('remark', models.CharField(max_length=50, verbose_name='备注')),
            ],
            options={
                'verbose_name': '轮播图表',
                'verbose_name_plural': '轮播图表',
                'db_table': 'slideshow',
            },
        ),
    ]
