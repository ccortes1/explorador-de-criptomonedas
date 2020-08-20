import scrapy

# name_cripto = '//div[@class="rows moz-hook"]//div[@class="trade-pair"]/text()'


class BitzSpider(scrapy.Spider):
    name = 'bitz'
    start_urls = [
        'https://www.bitz.so/'
    ]

    custom_settings={
        'FEED_URI': 'coinbase.json',
        'FEED_FORMAT': 'json',
        'FEED_EXPORT_ENCODING':'utf-8',
        'ROBOTSTXT_OBEY':False
    }

    def parse(self, response):
        name_cripto = response.xpath('//div[@class="rows moz-hook"]//div[@class="trade-pair"]/text()').getall()

        yield{
            'name_cripto': name_cripto
        }
