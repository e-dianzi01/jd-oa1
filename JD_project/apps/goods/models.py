from django.db import models

# Create your models here.
from users.models import JdShopper


# 创建商品详情表
class GoodsDetails(models.Model):
    m_id = models.ForeignKey(JdShopper, on_delete=models.CASCADE, verbose_name='店铺id')
    goods_id = models.IntegerField(verbose_name='商品编号', primary_key=True)
    goods_img = models.CharField(max_length=255, verbose_name='商品展示图片', blank=True, null=True)
    goods_name = models.CharField(max_length=200, verbose_name='商品名称', default='', blank=True, null=True)
    goods_prices = models.FloatField(max_length=50, verbose_name='商品单价', default=0, blank=True, null=True)
    kill_prices = models.FloatField(max_length=50, verbose_name='秒杀价格', default=0, blank=True, null=True)
    goods_num = models.IntegerField(verbose_name='商品库存', default=1, blank=True, null=True)
    goods_state = models.IntegerField(verbose_name='商品上架状态', default=1, choices=((0, '下架'), (1, '上架')), blank=True, null=True)
    one_category_id = models.IntegerField(verbose_name='一级分类id', blank=True, null=True)
    two_category_id = models.IntegerField(verbose_name='二级分类id', blank=True, null=True)
    keywords = models.CharField(max_length=50, verbose_name='关键字', blank=True, null=True)
    remark = models.CharField(max_length=255, verbose_name='备注', blank=True, null=True)
    sales = models.IntegerField(verbose_name='销量', default=0, blank=True, null=True)
    label = models.CharField(max_length=100, verbose_name='标签', blank=True, null=True)
    rate = models.CharField(max_length=100, verbose_name='好评率', blank=True, null=True)
    evaluate = models.IntegerField(verbose_name='评价条数', blank=True, null=True)

    def __str__(self):
        return self.goods_name

    class Meta:
        db_table = 'goods_details'
        verbose_name = '商品详细表'
        verbose_name_plural = verbose_name


class Main(models.Model):
    page_name = models.CharField(max_length=30, verbose_name='页面名称')
    img_urls = models.CharField(max_length=200, verbose_name='图片链接')
    remark = models.CharField(max_length=50, verbose_name='备注', blank=True, null=True)

    class Meta:
        abstract = True   # 定义为抽象模型，则不会将该模型迁移到数据库


# 创建轮播图表
class SlideShow(Main):
    def __str__(self):
        return self.page_name

    class Meta:
        db_table = 'slideshow'
        verbose_name = '轮播图表'
        verbose_name_plural = verbose_name


# 创建导航表
class Nav(Main):
    page_text = models.CharField(max_length=100, verbose_name='文字内容', blank=True, null=True)

    def __str__(self):
        return self.page_name

    class Meta:
        db_table = 'nav'
        verbose_name = '导航表'
        verbose_name_plural = verbose_name

#
# # 创建秒杀表
# class GoodsSeckill(models.Model):
#     goods_id = models.ForeignKey(GoodsDetails, on_delete=models.CASCADE, verbose_name='关联商品')
#     page_name = models.CharField(max_length=30, verbose_name='页面名称')
#     page_text = models.CharField(max_length=100, verbose_name='文字内容', blank=True, null=True)
#     kill_time = models.DateTimeField(verbose_name='秒杀时间', auto_now_add=True, blank=True, null=True)
#     remark = models.CharField(max_length=50, verbose_name='备注', blank=True, null=True)
#
#     def __str__(self):
#         return self.page_name
#
#     class Meta:
#         db_table = 'goods_seckill'
#         verbose_name = '秒杀表'
#         verbose_name_plural = verbose_name


# 创建商品推荐表
class GoodsRec(Main):
    one_category_id = models.IntegerField(verbose_name='推荐商品分类id')
    goods = models.ForeignKey(GoodsDetails, on_delete=models.CASCADE, verbose_name='关联商品')

    class Meta:
        db_table = 'goods_rec'
        verbose_name = '商品推荐表'
        verbose_name_plural = verbose_name


# 创建商品一级分类表
class GoodsType1(models.Model):
    one_type_id = models.IntegerField(verbose_name='一级分类id')
    one_type_name = models.CharField(max_length=20, verbose_name='一级分类名称', blank=True, null=True)
    remark = models.CharField(max_length=255, verbose_name='备注', blank=True, null=True)
    type_img = models.CharField(max_length=255, verbose_name='一级分类图片', blank=True, null=True)

    class Meta:
        db_table = 'goods_type1'
        verbose_name = '商品分类表'
        verbose_name_plural = verbose_name


# 创建商品二级分类表
class GoodsType2(models.Model):
    two_type_id = models.IntegerField(verbose_name='二级分类id')
    two_type_name = models.CharField(max_length=20, verbose_name='二级分类名称', blank=True, null=True)
    remark = models.CharField(max_length=255, verbose_name='备注', blank=True, null=True)
    type_img = models.CharField(max_length=255, verbose_name='二级分类图片', blank=True, null=True)

    class Meta:
        db_table = 'goods_type2'
        verbose_name = '商品分类表'
        verbose_name_plural = verbose_name


# 创建商品属性规格表
class GoodsSku(models.Model):
    goods_id = models.IntegerField(verbose_name='商品id')
    goods_num = models.IntegerField(verbose_name='商品库存', default=1, blank=True, null=True)
    properties = models.CharField(max_length=200, verbose_name='属性', blank=True, null=True)

    def __str__(self):
        return self.goods_id

    class Meta:
        db_table = 'goods_sku'
        verbose_name = '商品属性规格表'
        verbose_name_plural = verbose_name


# 创建商品图片表
class GoodsImages(models.Model):
    goods_id = models.ForeignKey(GoodsDetails, verbose_name='关联商品')
    img_urls = models.CharField(max_length=2000, verbose_name='商品详情图片', blank=True, null=True)

    def __str__(self):
        return self.goods_id

    class Meta:
        db_table = 'goods_imgs'
        verbose_name = '商品图片表'
        verbose_name_plural = verbose_name


# 创建拍卖表
class Auction(models.Model):
    goods_id = models.ForeignKey(GoodsDetails, verbose_name='商品id')
    describe = models.CharField(max_length=255, verbose_name='文字', blank=True, null=True)
    price = models.FloatField(verbose_name='拍卖价格')
    clickcount = models.IntegerField(verbose_name='访问数量', default=10)

    class Meta:
        db_table = 'goods_auction'
        verbose_name = '拍卖表'
        verbose_name_plural = verbose_name


# 创建优惠券表
class Coupon(models.Model):
    user_id = models.CharField(max_length=50, verbose_name='用户id', blank=True, null=True)
    cop_id = models.IntegerField(verbose_name='优惠券id')
    title = models.CharField(max_length=255, verbose_name='使用场景', blank=True, null=True)
    vuc = models.IntegerField(verbose_name='使用规则(0/1)',
                              default=0,
                              choices=((0, '无门槛优惠券'), (1, '满减优惠券')), blank=True, null=True)
    minusprice = models.FloatField(verbose_name='优惠价格', blank=True, null=True)

    class Meta:
        db_table = 'jd_coupon'
        verbose_name = '优惠券表'
        verbose_name_plural = verbose_name


# 商铺详情图片
class ShopperImg(models.Model):
    m_id = models.ForeignKey(JdShopper, on_delete=models.CASCADE, verbose_name='关联商户')
    img = models.CharField(max_length=2000, verbose_name='关联商品详细图片', blank=True, null=True)
    remark = models.CharField(max_length=100, verbose_name='图片类别', blank=True, null=True)

    class Meta:
        db_table = 'shopper_img'
        verbose_name = '商铺详情图片'
        verbose_name_plural = verbose_name
