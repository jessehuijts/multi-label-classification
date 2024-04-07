# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BolScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class Variables(scrapy.Item):
    categoryNames = scrapy.Field()
    title = scrapy.Field()
    subTitle = scrapy.Field()


