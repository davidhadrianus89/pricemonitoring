# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.serializers import json
from django.db import models
from django_extensions.db.models import TimeStampedModel

# Create your models here.


class ProductPage(TimeStampedModel):
    pageLink = models.TextField()

    def __str__(self):
        return self.pageLink


class Product(TimeStampedModel):
    pageLink = models.ForeignKey(ProductPage)
    name = models.CharField(max_length=255, null=True, blank=True)
    price = models.CharField(max_length=255, null=True, blank=True)
    old_price = models.CharField(max_length=255, null=True, blank=True)

    @property
    def to_dict(self):
        data = {
            'pageLink': json.loads(self.pageLink),
            'category': self.category,
            'name': self.name,
            'price': self.price,
        }
        return data

    def __str__(self):
        return self.pageLink.pageLink


class ProductDetail(TimeStampedModel):
    product = models.ForeignKey(Product)
    image = models.CharField(max_length=255, null=True, blank=True)
    descriptions = models.TextField(blank=True)





