from django.shortcuts import render
from django.db.models import Q

from apps.settings.models import Settings, About
from .models import Product, Category

# Create your views here.

def category(request):
    title_page = "Категории"
    categories = Category.objects.all().order_by("?")
    settings = Settings.objects.latest('id')
    return render(request, 'shop/shop-category.html', locals())

def category_detail(request, slug):
    title_page = "категория"
    settings = Settings.objects.latest('id')
    category = Category.objects.get(slug=slug)
    products = Product.objects.filter(category=category)
    return render(request, 'shop/shop-no-sidebar.html', locals())

def products(request):
    title_page = "Товары"
    categories = Category.objects.all()
    settings = Settings.objects.latest('id')
    all_products = Product.objects.all().order_by('?')
    about = About.objects.latest('id')
    return render(request, 'shop/all_products.html', locals())

def product_detail(request, id):
    title_page = "Товар"
    settings = Settings.objects.latest('id')
    product = Product.objects.get(id=id)
    about = About.objects.latest('id')
    return render(request, 'shop/product-details.html', locals())

def search(request):
    # title_page = "Поиск"
    setting = Settings.objects.latest('id')
    query = request.POST.get('query', '')
    if query:
        # Используйте Q-объекты для выполнения поиска в моделях Shop и Product
        all_products = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))

    return render(request, 'shop/all_products.html', locals())