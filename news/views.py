from django.shortcuts import render
from django.views import generic
from .models import Post
# from django.http import HttpResponse

# Create your views here.
#def daily_news(request):
#   return HttpResponse("Hello,news")

class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = "blog/index.html"
    paginate_by = 6
    