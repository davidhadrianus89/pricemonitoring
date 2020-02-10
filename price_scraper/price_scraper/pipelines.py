# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from productmonitoring.models import Product, ShopDetail


# class PriceScraperPipeline(object):
#
#     def process_item(self, item, spider):
#         try:
#             print ("ITEM", item)
#             product = Product.objects.get(pageLink__pageLink=item['pageLink'])
#             instance = item.save(commit=False)
#             product.pk = instance.pk
#             product.price = instance.price
#             product.old_price = instance.old_price
#         except Product.DoesNotExist:
#             pass
#         item.save()
#         return item


class PriceScraperPipeline(object):
    def process_item(self, item, spider):
        try:
            print("ITEM", item)
            shop = ShopDetail.objects.get(url=item['url'])
            instance = item.save(commit=False)
            shop.badge = instance.badge
            shop.total_feedback = instance.total_feedback
            shop.subscriber = instance.subscriber
            shop.join_date = instance.join_date
        except ShopDetail.DoesNotExist:
            pass
        item.save()
        return item

