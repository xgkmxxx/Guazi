# coding:utf-8
from django.shortcuts import render
from guazi.models import GuaziCar
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage
from django.db.models import Q

# Create your views here.

def list_guazi(request):
    after_range_num = 5
    before_range_num = 4
    page_size = 20
    Guazi_list = GuaziCar.objects.all().order_by('-id')
    paginator = Paginator(Guazi_list, page_size)
    try:
        page = int(request.GET.get('page','1'))
        if page < 1:
            page=1
    except ValueError:
        page=1
    try:
        carlist = paginator.page(page)
    except (EmptyPage,InvalidPage,PageNotAnInteger):
        carlist = paginator.page(1)
    if page >= after_range_num:
        page_range = list(paginator.page_range)[page-after_range_num:page+before_range_num]
    else:
        page_range = list(paginator.page_range)[0:int(page)+before_range_num]
    return render(request, 'guazi.html', {'guazi_list': carlist, 'page_range': page_range})

def search(request):
    query = request.GET.get('q','')
    page_size = 20
    after_range_num = 5
    before_range_num = 4
    if query:
        qset = (
                Q(name__icontains=query) |
                Q(city__icontains=query) |
                Q(time__icontains=query) |
                Q(mile__icontains=query) |
                Q(price__icontains=query)
            )
        result = GuaziCar.objects.filter(qset).distinct()
        paginator = Paginator(result, page_size)
        try:
            page = int(request.GET.get('page', '1'))
            if page < 1:
                page = 1
        except ValueError:
            page = 1
        try:
            contacts = paginator.page(page)
        except (EmptyPage,InvalidPage,PageNotAnInteger):
            contacts = paginator.page(paginator.num_pages)
        if page >= after_range_num:
            page_range = list(paginator.page_range)[page-after_range_num:page+before_range_num]
        else:
            page_range = list(paginator.page_range)[0:int(page)+before_range_num]
        return render(request, 'search.html', {'result': contacts, 'query': query, 
                                                'page_range': page_range })
    else:
        result = []
    return render(request, 'search.html', {})
