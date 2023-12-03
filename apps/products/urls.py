from django.urls import path 

from .views import *

urlpatterns = [
    path('products/', products, name='products'),
    path('category/', category, name='category'),
    path('product_list/', product_list, name='product_list'),
    path('category/<str:slug>/', category_detail, name="category_detail"),
    path('product_detail/<int:id>/', product_detail, name='product_detail'),
    path('search/', search, name='search'),
    path('compare/', compare_products_view, name='comparison_page'),
    path('compare_products/', compare_products, name='comparison'),
]