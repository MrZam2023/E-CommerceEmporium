from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.helloView),
    path('goodby/', views.goodbyView),
    path('date/', views.now_dateView),
    path('post/', views.postView),
    path('post_detail/<int:id>/', views.postDetailViews)
]