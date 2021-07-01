import urllib.request
import bs4
from agent.models.searched_item import *

class ScrapingMercari():
    def scraping_mercari(self,url_data):
        ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) '\
            'AppleWebKit/537.36 (KHTML, like Gecko) '\
            'Chrome/55.0.2883.95 Safari/537.36 '
    
        req = urllib.request.Request(url_data, headers={'User-Agent': ua})
        html = urllib.request.urlopen(req)
        bs = bs4.BeautifulSoup(html, "html.parser")
        item_name = bs.select_one("h1")
        price = bs.select_one(".item-price")
        seller = bs.select_one('.item-detail-table a')
        image_url = bs.select_one('.owl-lazy').get('data-src')
        url = url_data
        item_id = url_data
        site = 'メルカリ'
        return SearchedItem(item_name=item_name.text,item_id=item_id,image_urls=image_url,seller_name=seller.text,site=site,url=url,price=price.text)


