from common.database import SessionLocal
from agent.models.syuppin_item import *
from agent.engine.scraping import *

class Manage():

    def add_db(self,url):

        s = ScrapingMercari()
        scraping_data = s.scraping_mercari(url)

        db:SessionLocal() # DBセッションをオープン
        item = SyuppinItem(item_name=scraping_data.item_name,price=scraping_data.price,) # 格納する商品レコードを作成
        db.query(item) # DBに追加 
        db.commit() # 変更を確定
        db.close() # DBをクローズ
