from scrapy_djangoitem import DjangoItem
from productmonitoring.models import Product, ShopDetail


class PriceScraperItem(DjangoItem):

    django_model = Product


# class PriceScraperItem(DjangoItem):
#     django_model = ShopDetail
