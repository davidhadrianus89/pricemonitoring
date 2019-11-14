# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.serializers import json
from django.db import models
from django_extensions.db.models import TimeStampedModel

# Create your models here.


class ProductPage(TimeStampedModel):
    uniqueId = models.CharField(max_length=255)
    pageLink = models.TextField()

    def __str__(self):
        return self.uniqueId


class Product(TimeStampedModel):
    pageLink = models.ForeignKey(ProductPage)
    category = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    price = models.CharField(max_length=255, null=True, blank=True)

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
        return self.pageLink.uniqueId


class ProductDetail(TimeStampedModel):
    product = models.ForeignKey(Product)
    currentPrice = models.DecimalField(max_digits=12, decimal_places=2)
    descriptions = models.TextField(blank=True)





