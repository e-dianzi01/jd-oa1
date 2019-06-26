from django.db import models

# Create your models here.


class Main(models.Model):
    page_name = models.CharField(max_length=30, verbose_name='页面名称')
    img_urls = models.CharField(max_length=200, verbose_name='图片链接')
    remark = models.CharField(max_length=50, verbose_name='备注')

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


# 创建商品推荐表
class GoodsRec(Main):
    def __str__(self):
        return self.page_name

    class Meta:
        db_table = 'goods_rec'
        verbose_name = '商品推荐表'
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


# 创建商品详情表
class GoodsDetails(models.Model):
    m_id = models.IntegerField(verbose_name='店铺id')
    good_img = models.CharField(max_length=255, verbose_name='商品展示图片', null=True)
    goods_name = models.CharField(max_length=200, verbose_name='商品名称')
    goods_prices = models.FloatField(max_length=50, verbose_name='商品单价', default=0)
    kill_prices = models.FloatField(max_length=50, verbose_name='秒杀价格', default=0)
    goods_num = models.IntegerField(verbose_name='商品库存', default=1)
    goods_state = models.IntegerField(verbose_name='商品上架状态', default=0, choices=((0, '上架'), (1, '下架')))
    one_category_id = models.IntegerField(verbose_name='一级分类id')
    two_category_id = models.IntegerField(verbose_name='二级分类id')
    goods_no = models.CharField(max_length=50, verbose_name='商品编号')
    keywords = models.CharField(max_length=50, verbose_name='关键字')
    remark = models.CharField(max_length=255, verbose_name='备注', null=True)

    def __str__(self):
        return self.goods_name

    class Meta:
        db_table = 'goods_details'
        verbose_name = '商品详细表'
        verbose_name_plural = verbose_name


# 创建秒杀表
class GoodsSeckill(models.Model):
    goods_id = models.ForeignKey(GoodsDetails, on_delete=models.CASCADE)
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


# 创建商品分类表
class GoodsType(models.Model):
    goods_id = models.IntegerField(verbose_name='商品id')
    one_type_name = models.CharField(max_length=20, verbose_name='一级分类名称', null=True)
    two_type_name = models.CharField(max_length=20, verbose_name='二级分类名称', null=True)
    remark = models.CharField(max_length=50, verbose_name='备注', null=True)

    class Meta:
        db_table = 'goods_type'
        verbose_name = '商品分类表'
        verbose_name_plural = verbose_name


# 创建商品属性规格表
class GoodsSku(models.Model):
    goods_id = models.IntegerField(verbose_name='商品id')
    goods_num = models.IntegerField(verbose_name='商品库存', default=1)
    properties = models.CharField(max_length=50, verbose_name='属性', null=True)

    def __str__(self):
        return self.goods_id

    class Meta:
        db_table = 'goods_sku'
        verbose_name = '商品属性规格表'
        verbose_name_plural = verbose_name


# 创建商品图片表
class GoodsImages(models.Model):
    goods_id = models.IntegerField(verbose_name='商品id')
    img_urls = models.CharField(max_length=255, verbose_name='商品详情图片')

    def __str__(self):
        return self.goods_id

    class Meta:
        db_table = 'goods_imgs'
        verbose_name = '商品图片表'
        verbose_name_plural = verbose_name


# 创建商品评论表
class GoodsComment(models.Model):
    goods_id = models.IntegerField(verbose_name='商品id')
    user_id = models.IntegerField(verbose_name='用户id')
    order_id = models.IntegerField(verbose_name='订单id')
    m_id = models.IntegerField(verbose_name='店铺id')
    grade = models.IntegerField(verbose_name='评分', default=4)
    comment_content = models.CharField(max_length=255, verbose_name='评论内容',
                                       default='东西强烈好评')
    comment_time = models.DateTimeField(verbose_name='评论时间', auto_now_add=True)

    def __str__(self):
        return self.goods_id

    class Meta:
        db_table = 'goods_comment'
        verbose_name = '商品评论表'
        verbose_name_plural = verbose_name
