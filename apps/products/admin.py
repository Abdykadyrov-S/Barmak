from django.contrib import admin

from .models import Category, Product

# Register your models here.
admin.site.register(Product)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    search_fields = ('title', 'slug')