from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout

from apps.settings.models import Settings
from apps.users.models import User
from apps.products.models import Category

# Create your views here.
def register(request):
    settings = Settings.objects.latest('id')
    footer_categories = Category.objects.all().order_by('?')
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            if username and email and password and confirm_password:
                try:
                    user = User.objects.create(username = username, email = email)
                    user.set_password(password)
                    user.save()
                    user = User.objects.get(username = username)
                    user = authenticate(username = username, password = password)
                    login(request, user)
                    return redirect('index')
                except:
                    return redirect('register_error')
            else:
                return redirect('register_error')
        else:
            return redirect('register_error')
    context = {
        'settings' : settings,
    }
    return render(request, 'users/register.html', context)

def user_login(request):
    footer_categories = Category.objects.all().order_by('?')
    settings = Settings.objects.latest('id')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username = username)
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('index')
        except:
            return redirect('user_not_found')
    context = {
        'settings' : settings,
    }
    return render(request, 'users/login.html', context)

def profile(request, username):
    user = User.objects.get(username = username)
    settings = Settings.objects.latest('id')
    return render(request, 'users/profile.html', locals())


def logout_view(request):
    logout(request)
    return redirect('login')