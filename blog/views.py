from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def hello_world(request):
    return HttpResponse("<h1>Hello World</h1>")


def all_posts(request):
    posts = Post.objects.all()
    return render(request, "posts.html", {"posts": posts})
