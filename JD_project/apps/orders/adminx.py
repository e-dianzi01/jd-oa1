#
from orders.models import OrderDetail

__author__ = 'bob'
__date__ = '2019/6/26 15:44'
import xadmin as admin


class OrderDetailAdmin(object):
    list_display = ['o_num', 'o_user', 'o_goods', 'o_shopper', 'o_conn', 'o_total', 'o_time', 'o_status']
    search_fields = ['o_num', 'o_goods', 'o_status']
    list_per_page = 20
    model_icon = 'glyphicon glyphicon-list-alt'


admin.site.register(OrderDetail, OrderDetailAdmin)
