from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db.models import Q

from apps.settings.models import Settings, About
from .models import Product, Category, ReviewProduct

# Create your views here.

def category(request):
    title_page = "Категории"
    categories = Category.objects.all().order_by("?")
    settings = Settings.objects.latest('id')
    footer_categories = Category.objects.all().order_by('?')
    return render(request, 'shop/shop-category.html', locals())

def category_detail(request, slug):
    title_page = "категория"
    settings = Settings.objects.latest('id')
    category = Category.objects.get(slug=slug)
    products = Product.objects.filter(category=category)
    footer_categories = Category.objects.all().order_by('?')
    return render(request, 'shop/category-details.html', locals())

def products(request):
    title_page = "Товары"
    categories = Category.objects.all()
    settings = Settings.objects.latest('id')
    all_products = Product.objects.all().order_by('?')
    about = About.objects.latest('id')
    footer_categories = Category.objects.all().order_by('?')
    return render(request, 'shop/all_products.html', locals())

def product_detail(request, id):
    title_page = "Товар"
    settings = Settings.objects.latest('id')
    product = Product.objects.get(id=id)
    about = About.objects.latest('id')
    footer_categories = Category.objects.all().order_by('?')
    reviews = ReviewProduct.objects.filter(product=product).select_related('user')
    if request.method == "POST":
        user = request.user
        product = Product.objects.get(id=id)
        message = request.POST.get('message', '')

        ReviewProduct.objects.create(user=user, product=product, message=message)

        return redirect('product_detail', id=id)
    return render(request, 'shop/product-details.html', locals())

def product_list(request):
    settings = Settings.objects.latest('id')
    # all_products = Product.objects.all()
    print(request.GET.get('min_price'))
    user_prices = request.GET.get('min_price').replace(" ", "").split("-")
    print(user_prices)
    min_price = int(user_prices[0])
    max_price = int(user_prices[1])
    all_products = Product.objects.filter(price__range=(min_price, max_price))
    print(all_products)

    return render(request, 'shop/all_products.html', locals())


# def search(request):
#     settings = Settings.objects.latest('id')
#     footer_categories = Category.objects.all().order_by('?')
#     query = request.POST.get('query', '')
#     if query:
#         # Используйте Q-объекты для выполнения поиска в моделях Shop и Product
#         all_products = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))

#     return render(request, 'shop/all_products.html', locals())


def search(request):
    query = request.GET.get('q', '')
    if query:
        results = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
        data = list(results.values('title', 'description'))
        return JsonResponse(data, safe=False)
    return JsonResponse([])