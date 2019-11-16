# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from productmonitoring.models import Product

class PriceScraperPipeline(object):

    def process_item(self, item, spider):
        try:
            product = Product.objects.get(pageLink__pageLink=item['pageLink'])
            instance = item.save(commit=False)
            instance.pk = product.pk
            instance.price = product.price
            instance.old_price = product.old_price
        except Product.DoesNotExist:
            pass
        item.save()
        return item
