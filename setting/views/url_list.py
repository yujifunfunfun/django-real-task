from django.views import generic
import requests
from setting.models.url_list import *
from agent.manage.manage import *
from agent.models.url_list import *
from common.database import SessionLocal


class Scrapinng(generic.TemplateView):
    template_name = 'setting/url.html'

    def post(self,request):
        url = self.request.POST.get('url_list')
        url_list = url.split('\n')

        db = SessionLocal()
        db.query(UrlList).delete()

        for i in url_list:

            # u = UrlList(url_list=i)
            # u.save()

            url = UrlList(url_list=i) # 格納する商品レコードを作成
            db.add(url) # DBに追加 
            db.commit() # 変更を確定
            db.close() # DBをクローズ
    
    
         
        
        