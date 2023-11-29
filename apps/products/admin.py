from django.contrib import admin
from .models import Category, Product, Characteristic, ReviewProduct

admin.site.register(ReviewProduct)

class CharacteristicInline(admin.TabularInline):
    model = Characteristic
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'created')
    list_filter = ('category', 'created')
    search_fields = ('title', 'category__title')
    inlines = [CharacteristicInline]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    search_fields = ('title', 'slug')
