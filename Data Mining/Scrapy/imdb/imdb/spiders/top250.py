import scrapy


class Top250Spider(scrapy.Spider):
    name = 'top250'
    allowed_domains = ['www.imdb.com']
    start_urls = ['http://www.imdb.com/chart/top/']

    def parse(self, response):
        for i in response.css('.titleColumn'):
            title = i.css('a::text').get()
            year = i.css('span::text').get()
            movie_url = i.css('a::attr(href)').get()
            meta_data = {
                'title': title,
                'year': year.replace('(', '').replace(')', '')
            }
            yield response.follow(movie_url, callback=self.parse_info, meta=meta_data)

    def parse_info(self, response):
        title = response.meta['title']
        year = response.meta['year']
        duration = response.css('.subtext time::text').get().strip()
        genres = ', '.join(response.css('.subtext a:not(:last-child)::text').getall())
        director_name = response.css('h4:contains("Director") + a::text').get()
        director_url = response.css('h4:contains("Director") + a::attr(href)').get()

        meta_data = {
            'title': title,
            'year': year,
            'duration': duration,
            'genres': genres,
            'director': director_name,
        }

        yield response.follow(director_url, callback=self.parse_director, meta=meta_data, dont_filter=True)

    def parse_director(self, response):
        top_four_movies = ', '.join(response.css('.knownfor-title-role a::text').getall())

        yield {
            'title': response.meta['title'],
            'year': response.meta['year'],
            'duration': response.meta['duration'],
            'genres': response.meta['genres'],
            'director': response.meta['director'],
            'top_four_movies': top_four_movies
        }