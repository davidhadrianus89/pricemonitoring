# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils import timezone
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


class ShopDetail(models.Model):
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)
    crawled_date = models.DateTimeField(default=timezone.now)
    url = models.URLField()
    badge = models.CharField(max_length=255)
    total_feedback = models.IntegerField(null=True, blank=True)
    subscriber = models.IntegerField(null=True, blank=True)
    join_date = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        pass





