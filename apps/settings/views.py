from django.shortcuts import render, redirect

from .models import *
from apps.blog.models import News
from apps.products.models import Category, Product
from apps.telegram_bot.views import get_text


# Create your views here.
def index(request):
    title_page = "Главная страница"
    settings = Settings.objects.latest('id')
    slide = Slide.objects.all().order_by('?')
    about = About.objects.latest('id')
    categories = Category.objects.all().order_by('?')[:5]
    footer_categories = Category.objects.all().order_by('?')[:6]
    products = Product.objects.all().order_by('?')
    popular_products = Product.objects.all().order_by('?')[:8]
    featured_products = Product.objects.all().order_by('?')[:4]
    news = News.objects.all().order_by('?')[:6]
    all_products = Product.objects.all().order_by('?')
    return render(request, "base/index.html",locals())

def send_data(request):
    if request.method =="POST":
       fullinfo =  request.POST.get('fullinfo')
       name = request.POST.get('name')
       phone = request.POST.get('phone')
       quiz_3 = request.POST.get('quiz_3')

       get_text(
       f"""
Новая заявка:

Имя пользователя: {name}

Номер телефона: {phone}

Выбранные поля:

{fullinfo}
        """
    )
       return redirect("index")

def about(request):
    title_page = "О нас"
    settings = Settings.objects.latest('id')
    about = About.objects.latest('id')
    best_products = Product.objects.all().order_by('?')
    footer_categories = Category.objects.all().order_by('?')[:6]
    data = Data.objects.latest('id')
    return render(request, "base/about.html",locals())

def contact(request):
    title_page = "Контакты"
    settings = Settings.objects.latest('id')
    about = About.objects.latest('id')
    footer_categories = Category.objects.all().order_by('?')[:6]
    if request.method =="POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        cause = request.POST.get('cause')
        Contact.objects.create(name=name, phone=phone, message=message, cause=cause)

        get_text(f""" Оставлен отзыв 
                Имя пользователя: {name}
                Номер телефона: {phone}
                Причина: {cause}
                Сообщение: {message}
                """)
        return redirect('index')

    return render(request, "base/contact.html", locals())