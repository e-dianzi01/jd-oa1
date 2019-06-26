#
from orders.models import JdOrder, OrderDetail

__author__ = 'bob'
__date__ = '2019/6/26 15:44'
import xadmin as admin


class JdOrderAdmin(object):
    list_display = ['o_user', 'o_goods', 'o_price', 'o_time', 'o_status']
    search_fields = ['o_user', 'o_goods', 'o_price', 'o_time', 'o_status']
    list_per_page = 20
    model_icon = 'glyphicon glyphicon-th-list'


class OrderDetailAdmin(object):
    list_display = ['o_user', 'o_goods', 'o_shopper', 'o_addr', 'o_conn', 'o_price', 'o_time', 'o_status']
    search_fields = ['o_price', 'o_time', 'o_status']
    list_per_page = 20
    model_icon = 'glyphicon glyphicon-list-alt'


admin.site.register(JdOrder, JdOrderAdmin)
admin.site.register(OrderDetail, OrderDetailAdmin)
