from django.views import generic
import requests
from setting.models.url_list import *
from agent.manage.manage import *

class Scrapinng(generic.TemplateView):
    template_name = 'setting/url.html'


    def post(self,request):
        url = self.request.POST.get('url_list')
        url_list = url.split('\n')

        for i in url_list:

            u = UrlList(url_list=i)
            u.save()
        
        urls = UrlList.objects.values_list('url_list')

        for j in urls:
            m = Manage()
            m.add_db(j)
         
        
        