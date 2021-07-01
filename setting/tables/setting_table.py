import django_tables2 as tables
from django_tables2.utils import Accessor
from ..models.setting_table import *
from ..models.syuppin_item import *


class ItemTable(tables.Table):
    
    class Meta:
        model = SyuppinItem
        template_name = 'django_tables2/bootstrap4.html'
        orderable = False
        
        fields = ('item_name','price','seller_name','image_url1','url','site') 