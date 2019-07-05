from django.db import models

# Create your models here.
from goods.models import GoodsDetails
from users.action import mysql_save
from users.models import JdUser, JdShopper
from django.utils.safestring import mark_safe

"""
mysql_save("o_detail", "o_num", OrderDetail.o_num, "o_status", OrderDetail.o_status)
"""


# 创建订单详情表
class OrderDetail(models.Model):
    o_num = models.CharField(max_length=255, verbose_name='订单号', primary_key=True)
    o_user = models.ForeignKey(JdUser, on_delete=models.CASCADE, verbose_name='关联用户')
    o_addr = models.CharField(max_length=255, verbose_name='收货地址', default='', blank=True, null=True)
    o_conn = models.CharField(max_length=20, verbose_name='联系电话', default='', blank=True, null=True)
    o_time = models.DateTimeField(verbose_name='下单时间', auto_now_add=True, blank=True, null=True)
    o_status = models.IntegerField(verbose_name='订单状态', default=0, choices=((0, '待付款'),
                                                                            (1, '待收货'),
                                                                            (2, '待评价'),
                                                                            (3, '已失效')), blank=True, null=True)
    o_shopper = models.ForeignKey(JdShopper, on_delete=models.CASCADE, verbose_name='关联商户')
    o_total = models.FloatField(verbose_name='订单总价', blank=True, null=True)
    o_relpay = models.FloatField(verbose_name='实际支付', blank=True, null=True)

    def __str__(self):
        return self.o_user.user_name

    def shipments(self):
        link = 'http://10.35.162.133:9005/test/{}/1'.format(self.o_num)
        return mark_safe("<a href='{}'>发货</a>".format(link))
    shipments.short_description = '发货'

    def delete_(self):
        link = 'http://10.35.162.133:9005/test/{}/3'.format(self.o_num)
        return mark_safe("<a href='{}/'>删除</a>".format(link))
    shipments.short_description = '删除'

    class Meta:
        db_table = 'o_detail'
        verbose_name = '订单详情表'
        verbose_name_plural = verbose_name


# 创建商品订单表
class OrderList(models.Model):
    g_num = models.IntegerField(verbose_name='商品数量')
    g_price = models.FloatField(verbose_name='商品价格')
    o_num = models.ForeignKey(OrderDetail, verbose_name='关联订单详情表')
    o_goods = models.ForeignKey(GoodsDetails, on_delete=models.CASCADE, verbose_name='关联商品')

    class Meta:
        db_table = 'order_list'
        verbose_name = '商品订单表'
        verbose_name_plural = verbose_name


# 创建商品评论表
class GoodsComment(models.Model):
    goods_id = models.ForeignKey(GoodsDetails, on_delete=models.CASCADE, verbose_name='关联商品', default='')
    order_id = models.ForeignKey(OrderDetail, on_delete=models.CASCADE, verbose_name='关联订单', default='')
    grade = models.IntegerField(verbose_name='评分', default=4,
                                choices=((1, '*'),
                                         (2, '**'),
                                         (3, "***"),
                                         (4, "****"),
                                         (5, '*****')))
    comment_content = models.CharField(max_length=255, verbose_name='评论内容',
                                       default='东西强烈好评')
    comment_time = models.DateTimeField(verbose_name='评论时间', auto_now=True)

    class Meta:
        db_table = 'order_comment'
        verbose_name = '商品评论表'
        verbose_name_plural = verbose_name


# 创建拼购表
class GrouBuy(models.Model):
    goods_id = models.ForeignKey(GoodsDetails, on_delete=models.CASCADE, verbose_name='关联商品')
    order_id = models.ForeignKey(OrderDetail, on_delete=models.CASCADE, verbose_name='关联订单')
    gbn = models.IntegerField(verbose_name='允许拼够人数', default=10, blank=True, null=True)
    gbp = models.IntegerField(verbose_name='已拼购人数', default=0, blank=True, null=True)
    buy_price = models.FloatField(verbose_name='拼购价格', blank=True, null=True)

    class Meta:
        db_table = 'group_buy'
        verbose_name = '商品拼购表'
        verbose_name_plural = verbose_name
