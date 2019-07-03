#
from cart.models import JdCart

__author__ = 'bob'
__date__ = '2019/6/25 17:08'
import xadmin as admin


class JdCartAdmin(object):
    list_display = ['c_user', 'c_goods', 'c_shopper', 'c_goods_num', 'c_freight']
    search_fields = ['c_user', 'c_goods', 'c_shopper', 'c_goods_num', 'c_freight']
    list_per_page = 20
    model_icon = 'glyphicon glyphicon-shopping-cart'


admin.site.register(JdCart, JdCartAdmin)
