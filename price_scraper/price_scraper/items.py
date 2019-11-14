from scrapy_djangoitem import DjangoItem
from productmonitoring.models import Product


class PriceScraperItem(DjangoItem):

    django_model = Product
