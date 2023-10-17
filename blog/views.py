from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def helloView(requesst):
    return HttpResponse("<h1>Hello! Its my project</h1>")


def now_dateView(request):
    current_date = datetime.now().date()
    return HttpResponse(current_date)

def goodbyView(request):
    return HttpResponse('<h1>Goodby user</h1>')