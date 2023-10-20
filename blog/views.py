from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from . import models


def postView(request):
    post_value = models.Post.objects.all()
    html_file_name = 'post/post.html'
    context = {
        'post_key': post_value,
    }
    return render(request, html_file_name, context)

def helloView(request):
    return HttpResponse("<h1>Hello! Its my project</h1>")


def now_dateView(request):
    current_date = datetime.now().date()
    return HttpResponse(current_date)

def goodbyView(request):
    return HttpResponse('<h1>Goodby user</h1>')