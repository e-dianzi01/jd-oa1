from django.db import models

# Create your models here.

# Create your models here.
from goods.models import GoodsDetails
from users.models import JdUser, JdShopper


# 创建用户购物车
class JdCart(models.Model):
    c_user = models.ForeignKey(JdUser, on_delete=models.CASCADE, verbose_name='关联用户')
    c_goods = models.ForeignKey(GoodsDetails, on_delete=models.CASCADE, verbose_name='关联商品')
    c_goods_num = models.IntegerField(verbose_name='商品数量', default=1, blank=True, null=True)
    c_shopper = models.ForeignKey(JdShopper, on_delete=models.CASCADE, verbose_name='关联商家')
    c_freight = models.FloatField(verbose_name='运费', blank=True, null=True)

    class Meta:
        db_table = 'jd_cart'
        verbose_name = '用户购物车'
        verbose_name_plural = verbose_name
