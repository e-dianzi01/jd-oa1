from django.db import models

# Create your models here.


# 创建商品详情表
class GoodsDetails(models.Model):
    m_id = models.IntegerField(verbose_name='店铺id')
    good_img = models.CharField(max_length=255, verbose_name='商品展示图片', null=True)
    goods_name = models.CharField(max_length=200, verbose_name='商品名称', default='')
    goods_prices = models.FloatField(max_length=50, verbose_name='商品单价', default=0)
    kill_prices = models.FloatField(max_length=50, verbose_name='秒杀价格', default=0)
    goods_num = models.IntegerField(verbose_name='商品库存', default=1)
    goods_state = models.IntegerField(verbose_name='商品上架状态', default=0, choices=((0, '上架'), (1, '下架')))
    one_category_id = models.IntegerField(verbose_name='一级分类id')
    two_category_id = models.IntegerField(verbose_name='二级分类id')
    goods_id = models.IntegerField(verbose_name='商品编号', null=True)
    keywords = models.CharField(max_length=50, verbose_name='关键字')
    remark = models.CharField(max_length=255, verbose_name='备注', null=True)

    def __str__(self):
        return self.goods_name

    class Meta:
        db_table = 'goods_details'
        verbose_name = '商品详细表'
        verbose_name_plural = verbose_name


class Main(models.Model):
    page_name = models.CharField(max_length=30, verbose_name='页面名称', null=True)
    img_urls = models.CharField(max_length=200, verbose_name='图片链接', null=True)
    remark = models.CharField(max_length=50, verbose_name='备注', null=True)

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
    page_text = models.CharField(max_length=100, verbose_name='文字内容', null=True)

    def __str__(self):
        return self.page_name

    class Meta:
        db_table = 'nav'
        verbose_name = '导航表'
        verbose_name_plural = verbose_name


# 创建秒杀表
class GoodsSeckill(models.Model):
    goods_id = models.ForeignKey(GoodsDetails, on_delete=models.CASCADE, verbose_name='关联商品')
    page_name = models.CharField(max_length=30, verbose_name='页面名称')
    page_text = models.CharField(max_length=100, verbose_name='文字内容', null=True)
    kill_time = models.DateTimeField(verbose_name='秒杀时间', auto_now_add=True)
    remark = models.CharField(max_length=50, verbose_name='备注', null=True)

    def __str__(self):
        return self.page_name

    class Meta:
        db_table = 'goods_seckill'
        verbose_name = '秒杀表'
        verbose_name_plural = verbose_name


# 创建商品推荐表
class GoodsRec(Main):
    one_category_id = models.IntegerField(verbose_name='推荐商品分类id', null=True)
    goods = models.ForeignKey(GoodsDetails, on_delete=models.CASCADE, verbose_name='关联商品')

    class Meta:
        db_table = 'goods_rec'
        verbose_name = '商品推荐表'
        verbose_name_plural = verbose_name


# 创建商品一级分类表
class GoodsType1(models.Model):
    goods_id = models.IntegerField(verbose_name='商品id', null=True)
    one_type_name = models.CharField(max_length=20, verbose_name='一级分类名称', null=True)
    two_type_name = models.CharField(max_length=20, verbose_name='二级分类名称', null=True)
    remark = models.CharField(max_length=50, verbose_name='备注', null=True)
    type_img = models.CharField(max_length=255, verbose_name='一级分类图片', null=True)

    class Meta:
        db_table = 'goods_type1'
        verbose_name = '商品分类表'
        verbose_name_plural = verbose_name


# 创建商品二级分类表
class GoodsType2(models.Model):
    goods_id = models.IntegerField(verbose_name='商品id', null=True)
    one_type_name = models.CharField(max_length=20, verbose_name='一级分类名称', null=True)
    two_type_name = models.CharField(max_length=20, verbose_name='二级分类名称', null=True)
    remark = models.CharField(max_length=50, verbose_name='备注', null=True)
    type_img = models.CharField(max_length=255, verbose_name='二级分类图片', null=True)

    class Meta:
        db_table = 'goods_type2'
        verbose_name = '商品分类表'
        verbose_name_plural = verbose_name


# 创建商品属性规格表
class GoodsSku(models.Model):
    goods_id = models.IntegerField(verbose_name='商品id', null=True)
    goods_num = models.IntegerField(verbose_name='商品库存', default=1)
    properties = models.CharField(max_length=200, verbose_name='属性', null=True)

    def __str__(self):
        return self.goods_id

    class Meta:
        db_table = 'goods_sku'
        verbose_name = '商品属性规格表'
        verbose_name_plural = verbose_name


# 创建商品图片表
class GoodsImages(models.Model):
    goods_id = models.IntegerField(verbose_name='商品id', null=True)
    img_urls = models.CharField(max_length=255, verbose_name='商品详情图片')

    def __str__(self):
        return self.goods_id

    class Meta:
        db_table = 'goods_imgs'
        verbose_name = '商品图片表'
        verbose_name_plural = verbose_name


# 创建商品评论表
class GoodsComment(models.Model):
    goods_id = models.IntegerField(verbose_name='商品id', null=True)
    user_id = models.IntegerField(verbose_name='用户id', null=True)
    order_id = models.IntegerField(verbose_name='订单id', null=True)
    m_id = models.IntegerField(verbose_name='店铺id', null=True)
    grade = models.IntegerField(verbose_name='评分', default=4,
                                choices=((1, '*'),
                                         (2, '**'),
                                         (3, "***"),
                                         (4, "****"),
                                         (5, '*****')))
    comment_content = models.CharField(max_length=255, verbose_name='评论内容',
                                       default='东西强烈好评')
    comment_time = models.DateTimeField(verbose_name='评论时间', auto_now=True)

    def __str__(self):
        return self.goods_id

    class Meta:
        db_table = 'goods_comment'
        verbose_name = '商品评论表'
        verbose_name_plural = verbose_name


# 创建拍卖表
class Auction(models.Model):
    goods_id = models.IntegerField(verbose_name='商品id', null=True)
    img_url = models.CharField(max_length=255, verbose_name='商品图片', null=True)
    describe = models.CharField(max_length=255, verbose_name='文字', null=True)
    price = models.FloatField(verbose_name='拍卖价格')
    clickcount = models.IntegerField(verbose_name='访问数量', default=10)

    class Meta:
        db_table = 'goods_auction'
        verbose_name = '拍卖表'
        verbose_name_plural = verbose_name


# 创建优惠券表
class Coupon(models.Model):
    user_id = models.IntegerField(verbose_name='用户id')
    cop_id = models.IntegerField(verbose_name='优惠券id')
    title = models.CharField(max_length=255, verbose_name='使用场景', null=True)
    vuc = models.IntegerField(verbose_name='使用规则(0/1)',
                              default=0,
                              choices=((0, '无门槛优惠券'), (1, '满减优惠券')))
    minusprice = models.FloatField(verbose_name='优惠价格')

    class Meta:
        db_table = 'jd_coupon'
        verbose_name = '优惠券表'
        verbose_name_plural = verbose_name
