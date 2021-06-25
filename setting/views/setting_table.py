from ..models.setting_table import *
from django_tables2 import SingleTableView
from ..tables.setting_table import *
from ..models.setting_table import *


class SettingTableView(SingleTableView):
    table_class = ItemTable
    template_name = 'setting/setting_table.html'
    def get_queryset(self):
        return ItemData.objects.all()