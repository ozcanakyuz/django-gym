# from django.contrib import messages
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello")


