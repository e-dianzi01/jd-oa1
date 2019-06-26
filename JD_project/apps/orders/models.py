from django.db import models

# Create your models here.
from goods.models import GoodsDetails
from users.models import JdUser, JdShopper


# 创建订单列表
class JdOrder(models.Model):
    o_user = models.ForeignKey(JdUser, on_delete=models.CASCADE, verbose_name='关联用户', null=True)
    o_goods = models.ForeignKey(GoodsDetails, on_delete=models.CASCADE, verbose_name='关联商品', null=True)
    o_price = models.FloatField(verbose_name='订单总价', default=0)
    o_time = models.DateTimeField(verbose_name='下单时间', auto_now=True)
    o_status = models.IntegerField(verbose_name='订单状态', default=0, choices=((0, '待付款'), (1, '待收货'), (2, '待评价')))

    def __str__(self):
        return self.o_user.user_name

    class Meta:
        db_table = 'order'
        verbose_name = '订单列表'
        verbose_name_plural = verbose_name


# 创建订单详情表
class OrderDetail(models.Model):
    o_user = models.ForeignKey(JdUser, on_delete=models.CASCADE, verbose_name='关联用户', blank=True, null=True)
    o_goods = models.ForeignKey(GoodsDetails, on_delete=models.CASCADE, verbose_name='关联商品', blank=True, null=True)
    o_shopper = models.ForeignKey(JdShopper, on_delete=models.CASCADE, verbose_name='关联商户', blank=True, null=True)
    o_addr = models.CharField(max_length=255, verbose_name='收货地址', default='')
    o_conn = models.CharField(max_length=20, verbose_name='联系电话', default='')
    o_price = models.FloatField(verbose_name='商品价格', blank=True, null=True)
    o_time = models.DateTimeField(verbose_name='下单时间', auto_now=True)
    o_status = models.IntegerField(verbose_name='订单状态', default=0, choices=((0, '待付款'), (1, '待收货'), (2, '待评价')))

    def __str__(self):
        return self.o_user.user_name

    class Meta:
        db_table = 'order_detail'
        verbose_name = '订单详情表'
        verbose_name_plural = verbose_name
