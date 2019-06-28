from django.db import models

# Create your models here.


# Create your models here.
from JD_project.helper import make_password


# 创建客户端用户表
class JdUser(models.Model):
    user_name = models.CharField(max_length=50, verbose_name='用户名')
    user_id = models.CharField(max_length=50, verbose_name='用户ID')
    auth_string = models.CharField(max_length=255, verbose_name='用户密码', null=True)
    is_val = models.IntegerField(verbose_name='是否验证', default=0,
                                 choices=((0, '未验证'), (1, '已验证')))
    tel = models.CharField(max_length=15, verbose_name='联系电话', null=True)
    asset = models.FloatField(verbose_name='余额', default=0)
    u_img = models.ImageField(max_length=255, verbose_name='用户头像')
    u_bank = models.CharField(max_length=50, verbose_name='银行卡', null=True)
    user_card = models.CharField(max_length=50, verbose_name='身份证号', null=True)
    pay_pwd = models.CharField(max_length=6, verbose_name='支付密码', blank=True, null=True)
    u_email = models.CharField(max_length=20, verbose_name='邮箱', blank=True, null=True)
    u_real = models.CharField(max_length=20, verbose_name='真实姓名', blank=True, null=True)
    u_intg = models.IntegerField(verbose_name='用户积分')

    def __str__(self):
        return self.user_name

    class Meta:
        db_table = 'jd_user'
        verbose_name = '用户信息表'
        verbose_name_plural = verbose_name


# 创建客户端用户地址表
class UAddress(models.Model):
    user_id = models.IntegerField(verbose_name='用户ID')
    user_address = models.CharField(max_length=255, verbose_name='收货地址', blank=True, null=True)
    is_default = models.IntegerField(verbose_name='默认地址', default=0, choices=((0, '选择'), (1, '不选择')))

    class Meta:
        db_table = 'u_address'
        verbose_name = '地址表'
        verbose_name_plural = verbose_name


# 创建收藏商品表
class CollectGoods(models.Model):
    user_id = models.IntegerField(verbose_name='用户id')
    goods_no = models.IntegerField(verbose_name='商品编号')

    class Meta:
        db_table = 'u_clt_gs'
        verbose_name = '收藏商品表'
        verbose_name_plural = verbose_name


# 创建收藏商户表
class CollectShopper(models.Model):
    user_id = models.IntegerField(verbose_name='用户id')
    m_id = models.IntegerField(verbose_name='商户id')

    class Meta:
        db_table = 'u_clt_sp'
        verbose_name = '收藏商户表'
        verbose_name_plural = verbose_name


# 创建商户表
class JdShopper(models.Model):
    login_name = models.CharField(max_length=20, verbose_name='账号名', blank=True, null=True)
    login_auth_str = models.CharField(max_length=200, verbose_name='密码', blank=True, null=True)
    create_time = models.DateTimeField(verbose_name='注册时间',  auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)
    is_active = models.IntegerField(verbose_name='登陆状态', default=0, choices=((0, '未登录'), (1, '已登录')))
    note = models.CharField(max_length=50, verbose_name='备注', blank=True, null=True)
    m_id = models.CharField(max_length=20, verbose_name='商户ID')
    m_name = models.CharField(max_length=50, verbose_name='商铺名称')
    m_img = models.ImageField(upload_to='media', verbose_name='商户图片')
    m_email = models.CharField(max_length=50, verbose_name='商户邮箱', blank=True, null=True)
    m_phone = models.CharField(max_length=15, verbose_name='手机号', blank=True, null=True)
    s_add = models.CharField(max_length=255, verbose_name='地址', blank=True, null=True)
    is_delete = models.IntegerField(verbose_name='删除标志位', default=0, choices=((0, '未删除'), (1, '已删除')))

    def __str__(self):
        return self.login_name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if len(self.login_auth_str) < 32:
            self.login_auth_str = make_password(self.login_auth_str)
        super().save()

    def image_tag(self):
        return u'<img src="%s" />' % self.m_img

    class Meta:
        db_table = 'jd_shopper'
        verbose_name = '商户表'
        verbose_name_plural = verbose_name

