from django.urls import path 
from apps.users.views import register, user_login, logout_view, profile
from apps.users.allauth_providers import oauth2_login, oauth2_callback


urlpatterns = [
    path('register/', register, name = "register"),
    path('login/', user_login, name = "login"),
    path('profile/<str:username>/', profile, name = "profile"),
    path('logout/', logout_view, name = "logout"),
    path('accounts/google/login/', oauth2_login, name='google_login'),
    path('accounts/google/login/callback/', oauth2_callback, name='google_callback'),
]