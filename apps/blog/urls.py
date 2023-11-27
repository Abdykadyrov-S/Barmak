from django.urls import path

from .views import news_detail, news

urlpatterns = [
    path('news/', news, name="news"),
    path('news_detail/<int:id>/', news_detail, name="news_detail"),
]