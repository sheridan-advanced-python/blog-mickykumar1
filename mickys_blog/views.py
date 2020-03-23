# micky's Blog/views.py

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello world! Welcome to Micky\'s Blog!")
