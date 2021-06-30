import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
from common.database import SessionLocal
from agent.models.syuppin_item import *
from agent.engine.scraping import *
from agent.models.url_list import *



def add_db():
    
    s = ScrapingMercari()
    db = SessionLocal()

    # urls = UrlList.objects.values_list('url_list')
    urls = db.query(UrlList).all()

    for url in urls:
        scraping_data = s.scraping_mercari(url.url_list)

        item = SyuppinItem(item_name=scraping_data.item_name,price=scraping_data.price,seller_name=scraping_data.seller_name,image_url1=scraping_data.image_urls,url=scraping_data.url,site=scraping_data.site) # 格納する商品レコードを作成
        db.add(item) # DBに追加 
        db.commit() # 変更を確定

    db.close() # DBをクローズ
    print('ok')


if __name__ == "__main__":
    add_db()