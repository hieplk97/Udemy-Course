import os
import glob
from scrapy import Spider
from scrapy.http import Request
from advanced_books_crawler.items import AdvancedBooksCrawlerItem
from scrapy.loader import ItemLoader


def product_info(response, value):
    return response.xpath('//th[text()="' + value + '"]/following-sibling::td/text()').extract_first()


class BooksCrawlerSpider(Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    # scrapy crawl books_crawler -a category="[url]"
    # def __init__(self, category):
    #    self.start_urls = [category]

    def parse(self, response):
        books = response.xpath('//h3/a/@href').extract()
        for book in books:
            absolute_url = response.urljoin(book)
            yield Request(absolute_url, callback=self.parse_book)

        # process next page
        next_page_url = response.xpath('//a[text()="next"]/@href').extract_first()
        absolute_next_page_url = response.urljoin(next_page_url)
        yield Request(absolute_next_page_url)

    def parse_book(self, response):
        loader = ItemLoader(item=AdvancedBooksCrawlerItem(), response=response)

        title = response.css('h1::text').extract_first()
        price = response.xpath('//*[@class="price_color"]/text()').extract_first()

        image_urls = response.xpath('//img/@src').extract_first()
        image_urls = image_urls.replace('../..', 'http://books.toscrape.com/')

        rating = response.xpath('//*[contains(@class, "star-rating")]/@class').extract_first()
        rating = rating.replace('star-rating ', '')

        description = response.xpath('//*[@id="product_description"]/following-sibling::p/text()').extract_first()

        # Product information data
        upc = product_info(response, 'UPC')
        product_type = product_info(response, 'Product Type')
        price_without_tax = product_info(response, 'Price (excl. tax)')
        price_with_tax = product_info(response, 'Price (incl. tax)')
        tax = product_info(response, 'Tax')
        availability = product_info(response, 'Availability')
        number_of_reviews = product_info(response, 'Number of reviews')

        loader.add_value('title', title)
        loader.add_value('price', price)
        loader.add_value('image_urls', image_urls)
        loader.add_value('rating', rating)
        loader.add_value('description', description)
        loader.add_value('upc', upc)
        loader.add_value('product_type', product_type)
        loader.add_value('price_without_tax', price_without_tax)
        loader.add_value('price_with_tax', price_with_tax)
        loader.add_value('tax', tax)
        loader.add_value('availability', availability)
        loader.add_value('number_of_reviews', number_of_reviews)

        return loader.load_item()

    def close(self, reason):
        csv_file = max(glob.iglob('*.csv'), key=os.path.getctime)
        os.rename(csv_file, 'books.csv')
