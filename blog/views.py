from django.shortcuts import render, get_list_or_404, redirect
from django.http import HttpResponse
from datetime import datetime
from . import models
from .forms import CreatePostForm
from .models import Post


def post_view(request):

    if request.method == 'GET':
        search_text = request.GET.get('search')
        post_value = models.Post.objects.all()

        if search_text:
            """startwitch"""
            post_value = post_value.filter(tittle__startwitch=search_text)

        context_data = {
            'post_key': post_value,
            'user': request.user
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


def post_create_views(request):
    if request.method == 'GET':
        context_data = {
            'form': CreatePostForm
        }
        return render(request, 'post/create.html', context=context_data)

    if request.method == 'POST':
        data, files = request.POST, request.FILES
        form = CreatePostForm(data, files)

        if form.is_valid():
            cleaned_date = form.cleaned_data
            Post.objects.create(
                image=cleaned_date.get('image'),
                title = cleaned_date.get('title'),
                description = cleaned_date.get('description'),
                cost = cleaned_date.get('cost'),
                director = cleaned_date.get('director'),
                number_of_page = cleaned_date.get('number_of_page'),
            )
            return redirect('/post/')

        return render(request, 'post/create.html', context={'form': form})