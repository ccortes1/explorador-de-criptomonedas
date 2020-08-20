import scrapy

# name_cripto = '//tr/td/a/div/h4/text()'

class CoinbaseSpider(scrapy.Spider):
    name = 'coinbase'
    start_urls = [
        'https://www.coinbase.com/price'
    ]

    custom_settings={
        'FEED_URI': 'coinbase.json',
        'FEED_FORMAT': 'json',
        'FEED_EXPORT_ENCODING':'utf-8',
        'ROBOTSTXT_OBEY':False
    }

    def parse(self, response):
        name_cripto = response.xpath('//tr/td/a/div/h4/text()').getall()

        yield{
            'name_cripto': name_cripto
        }