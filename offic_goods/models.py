from django.db import models

# Create your models here.
#物品分类
class TypeInfo(models.Model):
    t_title = models.CharField('类别名称', max_length=20)
    isDelete = models.BooleanField(default=False)

#物品信息
class GoodsInfo(models.Model):
    g_title = models.CharField('物品名称', max_length=20)
    g_pic = models.ImageField(upload_to='of_goods')
    g_price = models.DecimalField('物品价格', max_digits=5, decimal_places=2)
    isDelete = models.BooleanField(default=False)
    g_unit = models.CharField('单位', max_length=20, default='500g')
    g_click = models.IntegerField('点击量')
    g_jianjie = models.CharField('简介', max_length=200)
    g_kucun = models.IntegerField('库存')
    g_content = models.CharField('物品详情', max_length=500)
    g_type = models.ForeignKey(TypeInfo)