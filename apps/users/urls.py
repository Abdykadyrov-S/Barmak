from django.urls import path 
from apps.users.views import register, user_login, logout_view, profile


urlpatterns = [
    path('register/', register, name = "register"),
    path('login/', user_login, name = "login"),
    path('profile/<str:username>/', profile, name = "profile"),
    path('logout/', logout_view, name = "logout"),
]