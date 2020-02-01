# mysite/views.py

from django.http import HttpResponse


def index(request):
    return HttpResponse('Micky\'s Blog!')
    return HttpResponse('Hello world!')
