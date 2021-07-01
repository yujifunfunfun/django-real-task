class SearchedItem():
    
    def __init__(self, 
                 item_name:str, item_id:str, image_urls:str, seller_name:str, site:str, url:str, price:str):
        self.item_name = item_name
        self.item_id = item_id
        self.image_urls = image_urls
        self.seller_name = seller_name
        self.is_remove = False
        self.site = site
        self.url = url
        self.price = price
        self.amazon_price = 0