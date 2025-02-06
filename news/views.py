from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def daily_news(request):
    return HttpResponse("Hello, news")
