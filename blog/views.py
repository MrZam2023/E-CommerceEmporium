from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse
from datetime import datetime
from . import models


def post_view(request):
    if request.method == 'GET':
        post_value = models.Post.objects.all()

        context_data = {
            'post_key': post_value
        }

        return render(request, 'post/post.html', context=context_data)


def hello_view(request):
    return HttpResponse("<h1>Hello! Its my project</h1>")


def now_date_view(request):
    current_date = datetime.now().date()
    return HttpResponse(current_date)


def goodby_view(request):
    return HttpResponse('<h1>Goodby user</h1>')


def post_detail_views(request, id):
    if request.method == 'GET':
        post = get_list_or_404(models.Post, id=id)

        context_data = {
            'post': post
        }

        return render(request, 'post/post_detail.html', context=context_data)