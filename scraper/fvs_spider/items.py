import scrapy
from scrapy.loader.processors import Join, MapCompose, TakeFirst

class FvSSpiderItem(scrapy.Item):
    isin     = scrapy.Field(output_processor=TakeFirst())
    price    = scrapy.Field(output_processor=TakeFirst())
    currency = scrapy.Field(output_processor=TakeFirst())
    datafrom = scrapy.Field(output_processor=TakeFirst())