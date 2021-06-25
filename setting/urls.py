from django.contrib import admin
from django.urls import path
from .views.sample_form import *
from .views.setting_table import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sample/', SampleFormView.as_view(), name="sample"),
    path('setting_table/', SettingTableView.as_view(), name="setting_table"),
]