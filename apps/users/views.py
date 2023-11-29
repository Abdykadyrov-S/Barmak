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
                    return redirect('profile')
                except:
                    return redirect('register')
            else:
                return redirect('register')
        else:
            return redirect('register')
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
            return redirect('login')
    context = {
        'settings' : settings,
    }
    return render(request, 'users/login.html', context)



def profile(request, username):
    user = User.objects.get(username = username)
    settings = Settings.objects.latest('id')

    if request.method == "POST":
        print("post")
        if 'update' in request.POST:
            username = request.POST.get('username')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            user.username = username 
            user.first_name = first_name
            user.last_name = last_name
            user.email = email 
            user.phone = phone 
            user.save()
            return redirect('profile', user.username)
        if 'update_profile_image' in request.POST:
            print("profil")
            profile_image = request.FILES.get('profile_image')
            print(profile_image)
            user.profile_image = profile_image
            if profile_image:
                user.profile_image = profile_image
                user.save()
                return redirect('profile', user.username)
        if 'delete' in request.POST:
            user.delete()
            return redirect('index')
        if 'update_password' in request.POST:
            password = request.POST.get('password')
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_password')
            if new_password == confirm_password:
                try:
                    user = User.objects.get(username = request.user)
                    if user.check_password(password):
                        user.set_password(new_password)
                        user.save()
                        return redirect('profile', user.username)
                    else:
                        return redirect('current_password_error')
                except:
                    return redirect('user_not_found')
            else:
                return redirect('passwords_are_different')
           
    return render(request, 'users/profile.html', locals())


def logout_view(request):
    logout(request)
    return redirect('login')