import django_tables2 as tables
from django_tables2.utils import Accessor
from ..models.setting_table import *

class ItemTable(tables.Table):
    
    class Meta:
        model = ItemData
        template_name = 'django_tables2/bootstrap4.html'
        orderable = False
        
        fields = ('account_name','item_name','price','item_id','image1','image2','image3','image4','auction') 