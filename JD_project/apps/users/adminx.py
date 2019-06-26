#
__author__ = 'bob'
__date__ = '2019/6/25 14:08'
import xadmin as admin

from xadmin import views
from users.models import LoginUser
from users.forms import LoginUserForm
# Register your models here.


class GlobalSetting(object):
    # 设置后台顶部标题
    site_title = '后台管理系统'
    # 设置后台底部标题   
    site_footer = 'www.JD.com'
    # 左侧菜单可以折叠
    menu_style = "accordion"


class LoginUserAdmin(object):
    form = LoginUserForm
    list_display = ['login_name', 'create_time', 'update_time']
    list_per_page = 20
    model_icon = 'glyphicon glyphicon-user'     # 添加模型图标


admin.site.register(LoginUser, LoginUserAdmin)
"""
class JdUserAdmin(object):
    form = JdUserForm
    list_display = ['user_id', 'user_name', 'nick_name',  'tel', 'is_login']
    list_per_page = 20


class JdShopperAdmin(object):
    form = JdUserForm
    list_display = ['m_id', 'm_name', 'm_username',  'm_email', 'm_phone']
    list_per_page = 20
"""



# 创建xadmin的最基本管理器配置，并与view绑定
class BaseSetting(object):
    # 开启主题功能
    enable_themes = True
    use_bootswatch = True


admin.site.register(views.CommAdminView, GlobalSetting)
admin.site.register(views.BaseAdminView, BaseSetting)