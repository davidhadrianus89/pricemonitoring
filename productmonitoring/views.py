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

from .models import Product


def index(request):
    if request.method == "POST":
        form = ProductPageForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            try:
                crawl(request, form.cleaned_data['pageLink'])
            except Exception as e:
                print 'GGGGG', str(e)
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
def crawl(request, url):
    if request.method == 'POST':
        domain = urlparse(url).netloc
        unique_id = str(uuid4())

        settings = {
            'unique_id': unique_id,
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
        print JsonResponse({'task_id': task, 'unique_id': unique_id, 'status': 'started'})
        return JsonResponse({'task_id': task, 'unique_id': unique_id, 'status': 'started'})
    elif request.method == 'GET':
        try:
            task_id = request.GET.get('task_id', None)
        except ValueError as e:
            return JsonResponse(
                {'error': e},
                status=HTTPException
            )
        try:
            unique_id = request.GET.get('unique_id', None)[:-1]
        except ValueError as e:
            return JsonResponse(
                {'error': e},
                status=HTTPException
            )
        status = scrapyd.job_status('default', task_id)
        if status == 'finished':
            pass
            try:
                item = ScrapyItem.objects.filter(unique_id=unique_id)
                if not item:
                    return JsonResponse(
                        {'error': 'There is no data'},
                        status=HTTPException
                    )
                dict_list = []
                for i in list(item):
                    dict_data = {
                        'url': i.url,
                        'title': i.title,
                        'contents': i.contents,
                        'published_date': i.published_date.strftime('%Y-%m-%d %H:%M'),
                        'views': i.views,
                        'recommends': i.recommends,
                        'date': i.date.strftime('%Y-%m-%d %H:%M')
                    }
                    dict_list.append(dict_data)
                data = {'data': dict_list}
                return JsonResponse(data)
            except Exception as e:
                return JsonResponse(
                    {'error': str(e)},
                )
        else:
            return JsonResponse({'status': status})
