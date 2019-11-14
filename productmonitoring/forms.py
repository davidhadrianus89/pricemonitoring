from __future__ import unicode_literals

from django import forms


from .models import ProductPage


class ProductPageForm(forms.ModelForm):

    class Meta:
        model = ProductPage
        fields = ('pageLink',)
