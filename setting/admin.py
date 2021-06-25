from django.contrib import admin

from .models.sample_form import *
from .models.setting_table import *

admin.site.register(SampleModel)
admin.site.register(ItemData)