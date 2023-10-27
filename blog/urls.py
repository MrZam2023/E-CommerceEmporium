from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_view),
    path('goodby/', views.goodby_view),
    path('date/', views.now_date_view),
    path('post/', views.post_view),
    path('post_detail/<int:id>/', views.post_detail_views)
]