# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class AdvancedBooksCrawlerPipeline:
    def process_item(self, item, spider):
        os.chdir('E:/Scrapy/advanced_books_crawler/images')
        if item['images'][0]['path']:
            new_image_name = ''.join(c for c in item['title'][0] if (c.isalnum() or c == ' ')) + '.jpg'
            new_image_path = 'full/' + new_image_name

            os.rename(item['images'][0]['path'], new_image_path)
