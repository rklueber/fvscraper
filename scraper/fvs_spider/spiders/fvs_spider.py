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
            
            isin =     fondsdata[i  ].xpath('td//text()')[1].get())
            price =    fondsprices[i].xpath('td//text()')[1].get().split(' ')[0])
            currency = fondsprices[i].xpath('td//text()')[1].get().split(' ')[1])
            datafrom = datetime.strptime(fondsprices[i].xpath('td//text()')[4].get(), "%d.%m.%Y").strftime("%Y-%m-%d"))
            
            print("=== ", isin, price, currency, datafrom)
            
            item = ItemLoader(FvSSpiderItem())
            item.add_value('isin',     isin)
            item.add_value('price',    price)
            item.add_value('currency', currency)
            item.add_value('datafrom', datafrom)
            yield item.load_item()
