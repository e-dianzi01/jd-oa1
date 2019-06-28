from django.db import models

# Create your models here.
from goods.models import GoodsDetails
from users.models import JdUser, JdShopper


# 创建订单详情表
class OrderDetail(models.Model):
    o_num = models.IntegerField(verbose_name='订单号')
    o_user = models.ForeignKey(JdUser, on_delete=models.CASCADE, verbose_name='关联用户', blank=True, null=True)
    o_addr = models.CharField(max_length=255, verbose_name='收货地址', default='')
    o_conn = models.CharField(max_length=20, verbose_name='联系电话', default='')
    o_time = models.DateTimeField(verbose_name='下单时间', auto_now_add=True)
    o_status = models.IntegerField(verbose_name='订单状态', default=0, choices=((0, '待付款'),
                                                                            (1, '待收货'),
                                                                            (2, '待评价')))
    o_shopper = models.ForeignKey(JdShopper, on_delete=models.CASCADE, verbose_name='关联商户', blank=True, null=True)
    o_goods = models.ForeignKey(GoodsDetails, on_delete=models.CASCADE, verbose_name='关联商品', blank=True, null=True)
    o_total = models.FloatField(verbose_name='订单总价', blank=True, null=True)
    o_relpay = models.FloatField(verbose_name='实际支付',blank=True, null=True)

    def __str__(self):
        return self.o_user.user_name

    class Meta:
        db_table = 'o_detail'
        verbose_name = '订单详情表'
        verbose_name_plural = verbose_name
