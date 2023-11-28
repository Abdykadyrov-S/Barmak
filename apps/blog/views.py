from django.shortcuts import render
from .models import *
from apps.settings.models import Settings, About
from apps.products.models import Category

# Create your views here.
def news(request):
    settings = Settings.objects.latest('id')
    about = About.objects.latest('id')
    news = News.objects.all()
    footer_categories = Category.objects.all().order_by('?')
    return render(request, "blog/blog.html",locals())

def news_detail(request,id):
    settings = Settings.objects.latest('id')
    about = About.objects.latest('id')
    news_others = News.objects.all().order_by('?')[:3]
    news = News.objects.get(id=id)
    footer_categories = Category.objects.all().order_by('?')
    return render(request, "blog/blog-details.html",locals())