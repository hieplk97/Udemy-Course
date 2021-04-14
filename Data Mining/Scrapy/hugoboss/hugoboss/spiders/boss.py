import scrapy
from scrapy import Request


class BossSpider(scrapy.Spider):
    name = 'boss'
    allowed_domains = ['www.hugoboss.com']
    start_urls = ['http://www.hugoboss.com/men/']

    def parse(self, response):
        css_selector = 'a[href="https://www.hugoboss.com/men-clothing/"] + div .col-xl-offset-1 a::attr(href)'
        for url in response.css(css_selector).getall():
            yield Request(url, callback=self.parse_products)
            break

    def parse_products(self, response):
        css_selector = '.product-tile-default__gallery a::attr(href)'
        for product_url in response.css(css_selector).getall():
            yield response.follow(product_url, callback=self.parse_product_detail)

        next_page_css = '.button.button--pagingbar.font__nav-link::attr(href)'
        next_page_url = response.css(next_page_css).get()
        if next_page_url:
            yield Request(next_page_url, callback=self.parse_products)

    def parse_product_detail(self, response):
        print(response.url)
        product_name = response.css('.stage__header-title::text').get()
        product_name = product_name.replace('\n', '')

        product_colors = response.css('.swatch-list__container .swatch-list__image::attr(title)').getall()
        product_colors = ', '.join(product_colors)

        product_picture_urls = ''

        for i in response.css('.stage__images-thumbnail-image::attr(src)').getall():
            product_picture_urls = i.split('?')[0] + '?wid=462&qlt=80' + ', '

        product_description = response.css('.product-container__item--description::text').get()
        product_description = product_description.replace('\n', '').strip()

        care_info = response.css('.care-info__text::text').getall()
        care_info = ', '.join(care_info)

        yield {
            'product_name': product_name,
            'product_colors': product_colors,
            'product_picture_urls': product_picture_urls,
            'product_description': product_description,
            'care_info': care_info
        }
