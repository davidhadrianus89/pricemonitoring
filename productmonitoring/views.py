from httplib import HTTPException
from urlparse import urlparse
from uuid import uuid4

import scrapyd
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils.translation import ugettext as _
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView
from scrapyd_api import ScrapydAPI

from .forms import ProductPageForm

from .models import Product, ProductPage


def index(request):
    if request.method == "POST":
        form = ProductPageForm(request.POST)
        if form.is_valid():
            try:
                instance = ProductPage.objects.get(pageLink=form.cleaned_data['pageLink'])
                instance.pageLink = form.cleaned_data['pageLink']
                instance.save()
            except ProductPage.DoesNotExist:
                form.save()
            try:
                crawl_post(request, form.cleaned_data['pageLink'])
            except Exception as e:
                pass
            return redirect('productmonitoring:product_list')
    else:
        form = ProductPageForm()
    return render(request, 'productmonitoring/productmonitoring.html', {'form': form})


class ProductListView(ListView):
    template_name = 'productmonitoring/productmonitoring_list.html'
    model = Product


def is_valid_url(url):
    validate = URLValidator()
    try:
        validate(url)
    except ValidationError:
        return False

    return True


class SchedulingError(Exception):
    def __str__(self):
        return 'scheduling error'


scrapyd = ScrapydAPI('http://localhost:6800')

@csrf_exempt
@require_http_methods(['POST', 'GET'])
def crawl_post(request, url):
    domain = urlparse(url).netloc

    settings = {
        'USER_AGENT': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
    }
    try:
        task = scrapyd.schedule('default', 'FabelioScraper', settings=settings, url=url, domain=domain)
        print task
    except SchedulingError as e:
        return JsonResponse(
            {'error': e},
            status=HTTPException
        )
    return JsonResponse({'task_id': task, 'status': 'started'})