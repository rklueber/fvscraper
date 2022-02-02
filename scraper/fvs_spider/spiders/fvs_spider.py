from scrapy import Request, Spider
from scrapy.loader import ItemLoader
from fvs_spider.items import FvSSpiderItem
from datetime import datetime

class FvSSpider(Spider):
    name = 'fvs'

    start_urls = [
            'https://lu.fvsinvest.lu/en/other/'
        ]

    def parse(self, response):
        fondsdata = response.css('div[data-id]')[0].css('tr')
        fondsprices = response.css('div[data-id]')[1].css('tr')
        for i in range(1,len(fondsdata)):

            isin =     fondsdata[i  ].xpath('td//text()')[1].get()
            datafrom = fondsprices[i].xpath('td//text()')[4].get()
            price =    fondsprices[i].xpath('td//text()')[1].get()

            if price != ' EUR':
                price    = price.split(' ')[0] 
                currency = price.split(' ')[1]
            else:
                price = 0
                currency = "EUR"
                        
            print("=== ", i, isin, price, currency, datafrom)
            
            item = ItemLoader(FvSSpiderItem())
            item.add_value('isin',     isin)
            item.add_value('price',    price)
            item.add_value('currency', currency)
            item.add_value('datafrom', datetime.strptime(datafrom, "%d.%m.%Y").strftime("%Y-%m-%d"))
            yield item.load_item()
