# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv
from itemadapter import ItemAdapter
from BolWebScraper.items import Variables


class BolWebScraperPipeline:
    def __init__(self):
        self.file = None
        self.writer = None

    def open_spider(self, spider):
        self.file = open('scraped_data.csv', 'w', newline='', encoding='utf-8')
        self.writer = csv.writer(self.file)
        self.writer.writerow(ItemAdapter(Variables()).field_names())

    def close_spider(self, spider):
        if self.file:
            self.file.close()

    def process_item(self, item, spider):
        if isinstance(item, Variables):
            row = ItemAdapter(item).values()
            self.writer.writerow(row)
        return item