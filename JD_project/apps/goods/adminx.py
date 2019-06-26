#
from goods.models import GoodsDetails

__author__ = 'bob'
__date__ = '2019/6/26 15:44'
import xadmin as admin


class GoodsDetailsAdmin(object):
    list_display = ['good_img', 'goods_no', 'goods_name', 'goods_prices', 'goods_num', 'goods_state']
    search_fields = ['goods_no', 'goods_name', 'goods_prices', 'goods_num']
    list_per_page = 20
    model_icon = 'glyphicon glyphicon-th'    # 添加模型图标


admin.site.register(GoodsDetails, GoodsDetailsAdmin)
