from django.db import models

class SyuppinItem(models.Model):
    item_name = models.CharField(max_length=10,verbose_name='商品名')
    price = models.CharField(max_length=10,verbose_name='価格')
    seller_name = models.CharField(max_length=50,verbose_name='販売者名')
    image_url1 = models.CharField(max_length=50,verbose_name='画像URL')
    url = models.CharField(max_length=50,verbose_name='URL')
    site = models.CharField(max_length=10,verbose_name='サイト')

    class Meta:
        db_table='a_syuppin_item'


