from django.http import HttpResponse
from django.shortcuts import render

from home.models import Setting

# Create your views here.

def index(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting,
               'page': 'Home',}
    return render(request, 'index.html', context)

def about(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting,
               'page': 'About',}
    return render(request, 'about.html', context)

def feature(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting,
               'page': 'Feature',}
    return render(request, 'feature.html', context)

def classes(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting,
               'page': 'Classes',}
    return render(request, 'classes.html', context)

def contact(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting,
               'page': 'Contact',}
    return render(request, 'contact.html', context)