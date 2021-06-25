from django.db import models

AUCTION=(
    ("メルカリ","メルカリ"),
    ("ラクマ","ラクマ"),
)

class ItemData(models.Model):
    account_name = models.CharField(max_length=10,verbose_name='ツールのアカウント名')
    item_name = models.CharField(max_length=10,verbose_name='商品名')
    price = models.CharField(max_length=10,verbose_name='価格')
    item_id = models.CharField(max_length=10,verbose_name='商品の個別ID')
    image1 = models.ImageField(upload_to='')
    image2 = models.ImageField(upload_to='')
    image3 = models.ImageField(upload_to='')
    image4 = models.ImageField(upload_to='')
    auction = models.CharField(max_length=10,default="メルカリ",verbose_name="メルカリ/ラクマ選択",choices=AUCTION)