from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import ProductPage, Product, ShopDetail


class ProductPageAdmin(admin.ModelAdmin):
    list_display = [
        'created',
        'modified',
        'pageLink'
    ]
    ordering = ['-created']


class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'created',
        'modified',
        'name',
        'price'
    ]
    ordering = ['-created']


class ShopDetailAdmin(admin.ModelAdmin):
    list_display = [
        'created',
        'updated',
        'crawled_date',
        'url'
    ]
    ordering = ['-created']


admin.site.register(ProductPage, ProductPageAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ShopDetail, ShopDetailAdmin)
