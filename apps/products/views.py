from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.db.models import Q

from apps.settings.models import Settings, About
from .models import Product, Category, ReviewProduct

import json

# Create your views here.
# def category(request):
#     title_page = "Категории"
#     categories = Category.objects.filter(parent=None).order_by("?")
#     settings = Settings.objects.latest('id')
#     footer_categories = Category.objects.all().order_by('?')
#     return render(request, 'shop/shop-category.html', locals())

def category(request):
    title_page = "Категории"
    categories = Category.objects.filter(parent=None).order_by("?")
    settings = Settings.objects.latest('id')
    footer_categories = Category.objects.all().order_by('?')
    return render(request, 'shop/shop-category.html', locals())

def sub_category(request):
    title_page = "Под Категории"
    parent_slug = request.GET.get('parent_slug')  # Получаем значение parent_slug из запроса
    if parent_slug:
        parent_category = get_object_or_404(Category, slug=parent_slug)
        subcategories = parent_category.subcategories.all()
    else:
        subcategories = Category.objects.filter(parent=None)
    settings = Settings.objects.latest('id')
    footer_categories = Category.objects.all().order_by('?')
    return render(request, 'shop/sub-category.html', locals())

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
    title_page = "Сортировка товаров"
    settings = Settings.objects.latest('id')
    all_products = Product.objects.all()
    footer_categories = Category.objects.all().order_by('?')

    print(request.GET.get('min_price'))
    min_price_param = request.GET.get('min_price')
    if min_price_param is not None:
        try:
            print(request.GET.get('min_price'))
            user_prices = request.GET.get('min_price').replace(" ", "").split("-")
            print(user_prices)
            min_price = int(user_prices[0])
            max_price = int(user_prices[1])
            all_products = Product.objects.filter(price__range=(min_price, max_price))
            print(all_products)
        except (ValueError, IndexError):
            pass

    popular = request.GET.get('popular', False)
    product_day = request.GET.get('product_day', False)
    new = request.GET.get('new', False)
    featured = request.GET.get('featured', False)

    if popular:
        all_products = all_products.filter(popular=True)
    if product_day:
        all_products = all_products.filter(product_day=True)
    if new:
        all_products = all_products.filter(new=True)
    if featured:
        all_products = all_products.filter(featured=True)

    return render(request, 'shop/all_products.html', locals())


def search(request):
    query = request.GET.get('q', '')
    if query:
        results = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query) | Q(image__icontains=query)).order_by('-created')[:5]
        print(results.values('id', 'title', 'description', 'image'))
        data = list(results.values('id', 'title', 'description', 'image')) 
        return JsonResponse(data, safe=False)
    return JsonResponse([])


def compare_products_view(request):
    title_page = "Сравнение товаров"
    settings = Settings.objects.latest('id')
    footer_categories = Category.objects.all().order_by('?')

    compare_list = request.session.get('compare_list', [])
    products_to_compare = Product.objects.filter(id__in=compare_list)

    return render(request, 'shop/compare.html', locals())



@require_http_methods(["POST"])
def compare_products(request):
    try:
        data = json.loads(request.body)
        product_id = data.get('product_id')
        action = data.get('action')

        if not product_id or not action:
            return JsonResponse({'status': 'error', 'message': 'Отсутствуют обязательные параметры'}, status=400)

        compare_list = request.session.get('compare_list', [])

        if action == 'add':
            if product_id not in compare_list:
                compare_list.append(product_id)
            message = 'Товар успешно добавлен'
        elif action == 'remove':
            if product_id in compare_list:
                compare_list.remove(product_id)
            message = 'Товар успешно удален'

        request.session['compare_list'] = compare_list
        return JsonResponse({'status': 'success', 'message': message})

    except json.JSONDecodeError:
        return JsonResponse({'status': 'error', 'message': 'Неверный формат данных'}, status=400)
# test