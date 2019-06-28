#
__author__ = 'bob'
__date__ = '2019/6/25 14:08'
import xadmin as admin

from xadmin import views
from users.models import JdShopper
from users.forms import JdShopperForm


# Register your models here.


class GlobalSetting(object):
    # 设置后台顶部标题
    site_title = '后台管理系统'
    # 设置后台底部标题   
    site_footer = 'www.JD.com'
    # 左侧菜单可以折叠
    menu_style = "accordion"


class JdShopperAdmin(object):
    form = JdShopperForm
    list_display = ['m_id','login_name', 'create_time', 'm_name', 'is_active', '']
    list_per_page = 20
    model_icon = 'glyphicon glyphicon-user'     # 添加模型图标


admin.site.register(JdShopper, JdShopperAdmin)


"""
"""


# 创建xadmin的最基本管理器配置，并与view绑定
class BaseSetting(object):
    # 开启主题功能
    enable_themes = True
    use_bootswatch = True


admin.site.register(views.CommAdminView, GlobalSetting)
admin.site.register(views.BaseAdminView, BaseSetting)
