from __future__ import unicode_literals

from django import forms


from .models import ProductPage, ShopDetail


class ProductPageForm(forms.ModelForm):

    class Meta:
        model = ProductPage
        fields = ('pageLink',)


# class ShopDetailForm(forms.ModelForm):
#
#     class Meta:
#         model = ShopDetail
#         fields = ('url',)
