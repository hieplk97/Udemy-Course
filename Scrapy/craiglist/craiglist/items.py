# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CraiglistItem(scrapy.Item):
    # define the fields for your item here like:
    date = scrapy.Field()
    link = scrapy.Field()
    text = scrapy.Field()
    compensation = scrapy.Field()
    employment_type = scrapy.Field()
    images = scrapy.Field()
    description = scrapy.Field()
