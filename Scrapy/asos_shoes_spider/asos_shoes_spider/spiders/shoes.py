from scrapy import Spider
from scrapy.http import Request
import json


class ShoesSpider(Spider):
    name = 'shoes'
    allowed_domains = ['asos.com']
    start_urls = ['https://www.asos.com/men/shoes-boots-trainers/shoes/cat/?cid=27116&nlid=mw|shoes|shop+by+product/']

    def parse(self, response):
        products = response.xpath('//article[@data-auto-id="productTile"]/a/@href').extract()
        for product in products:
            yield Request(product, callback=self.parse_shoes)

        next_page_url = response.xpath('//a[text()="Load more"]/@href').extract_first()
        if next_page_url:
            yield Request(next_page_url, callback=self.parse)

    def parse_shoes(self, response):
        product_name = response.xpath('//h1/text()').extract_first()
        product_id = response.url.split('/prd/')[1].split('?')[0]
        price_api_url = 'https://www.asos.com/api/product/catalogue/v3/stockprice?productIds=14187879&store=ROW&currency=GBP' + product_id

        yield Request(price_api_url, meta={'product_name': product_name}, callback=self.parse_shoes_price)

    def parse_shoes_price(self, response):
        json_response = json.load(response.body.decode('utf-8'))
        price = json_response[0]['productPrice']['current']['text']

        yield {
            'product_name': response.meta['product_name'],
            'price': price
        }
