from decimal import Decimal

import scrapy
from price_scraper.items import PriceScraperItem
from scrapy.spiders import CrawlSpider, Rule

from productmonitoring.models import ProductPage


class FabelioScraper(CrawlSpider):
    name = 'FabelioScraper'

    def __init__(self, *args, **kwargs):
        self.url = kwargs.get('url')
        self.domain = kwargs.get('domain')
        self.start_urls = [self.url]
        self.allowed_domains = [self.domain]

        super(FabelioScraper, self).__init__(*args, **kwargs)

    def parse(self, response):
        data = response.xpath('//div[@class = "columns"]')
        for line in data:
            item = PriceScraperItem()
            product_page = ProductPage.objects.filter(pageLink=self.url).first()
            item['pageLink'] = product_page
            item['name'] = line.xpath('//div[@class = "page-title__secondary"]//text()').extract_first()
            item['price'] = line.xpath('//span[@class="price"]/text()').extract_first()
            item['old_price'] = line.xpath('//span[@class="price"]/text()').extract()[1]
            yield item

