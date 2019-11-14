from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import ProductPage, Product


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


admin.site.register(ProductPage, ProductPageAdmin)
admin.site.register(Product, ProductAdmin)
