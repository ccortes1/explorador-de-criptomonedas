import scrapy

# name_cripto = '//div[@class="rows moz-hook"]//div[@class="trade-pair"]/text()'


class BinanceSpider(scrapy.Spider):
    name = 'binance'
    start_urls = [
        'https://www.binance.com/en/markets'
    ]

    custom_settings = {
        'FEED_URI': 'coinbase.json',
        'FEED_FORMAT': 'json',
        'FEED_EXPORT_ENCODING': 'utf-8',
        'ROBOTSTXT_OBEY': False
    }

    def parse(self, response):
        name_cripto = response.xpath(
            '//div[@class="rows moz-hook"]//div[@class="trade-pair"]/text()').getall()

        yield{
            'name_cripto': name_cripto
        }


