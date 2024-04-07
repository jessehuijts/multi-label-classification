from scrapy.spiders import SitemapSpider

from scrapy.loader import ItemLoader
from BolWebScraper.items import Variables


def extract_with_css(response, query):
    return response.css(query).get(default='').strip()


class BolSitemapSpider(SitemapSpider):
    name = 'bol_item_category'
    sitemap_urls = ['https://www.bol.com/sitemap/nl-nl/']
    sitemap_follow = ['product-121'] 

    def parse(self, response):
        loader = ItemLoader(item=Variables(), response=response)

        categoryNames = []  # Create an empty list to store multiple category names

        for category in response.css('ul.specs__categories > li.specs__category'):
            categoryName = extract_with_css(category, 'a::attr(title)')
            if categoryName is not None:
                categoryNames.append(categoryName)

        if categoryNames:
            loader.add_value('categoryNames', categoryNames)

        title = response.css('h1.page-heading > span[data-test=title]')
        fullTitle = extract_with_css(title, '::text')

        if fullTitle is not None:
            loader.add_value('title', fullTitle)

        subtitle = response.css('h1.page-heading > span[data-test=subtitle]')
        fullSubTitle = extract_with_css(subtitle, '::text')

        if fullSubTitle is not None:
            loader.add_value('subTitle', fullSubTitle)


        return loader.load_item()
