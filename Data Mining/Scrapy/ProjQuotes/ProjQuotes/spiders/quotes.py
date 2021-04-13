import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        # print("RESPONSE FROM SERVER:", response.url)
        # print("STATUS FROM SERVER:", response.status)

        # print("HEADER FROM SERVER:", response.headers)
        # print("VALUE FROM HEADER:", response.headers.get('Server').decode('utf-8'))
        # print("VALUE FROM HEADER:", response.headers.get('Content-Type').decode('utf-8'))

        # print("VALUE FROM BODY:", response.body.decode('utf-8'))
        # print("REQUEST OF RESPONSE:", response.request)
        # print("IP of SERVER:", response.ip_address)

        for div in response.css('.quote'):
            quote = div.css('.text::text').get()
            author = div.css('.author::text').get()
            tags = div.css('.tag::text').getall()
            yield {
                "quote": quote.replace(',', '').replace('”', '').replace('“', ''),
                "author": author,
                'tags': tags
            }

        next_page_url = response.css('li.next a::attr(href)').get()
        if next_page_url:
            print(next_page_url)
            yield response.follow(next_page_url, callback=self.parse)
        else:
            pass
        print("\n\n-------------------")
