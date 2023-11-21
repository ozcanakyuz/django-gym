from django.http import HttpResponse
from django.shortcuts import render

from home.models import Setting

# Create your views here.

def index(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting,
               'page': 'home',}
    return render(request, 'index.html', context)

def about(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting,
               'page': 'about',}
    return render(request, 'about.html', context)

def feature(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting,
               'page': 'feature',}
    return render(request, 'feature.html', context)