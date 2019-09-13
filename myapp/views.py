import requests
from django.shortcuts import render
from bs4 import BeautifulSoup


def home(request):
    context = {}
    return render(request, 'base.html',context)


def new_search(request):
    search = request.POST.get('search')
    context = {
        'search':search
    }
    return render(request, 'myapp/new_search.html', context)