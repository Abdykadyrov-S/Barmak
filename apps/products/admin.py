from django.contrib import admin
from .models import Category, Product, Characteristic, ReviewProduct, ImagesProduct

admin.site.register(ReviewProduct)

class CharacteristicInline(admin.TabularInline):
    model = Characteristic
    extra = 1

class ImagesProductInline(admin.TabularInline):
    model = ImagesProduct
    extra = 1

class CategoryInline(admin.TabularInline):
    model = Product.category.through
    extra = 1
    verbose_name = 'категории продукта'
    verbose_name_plural = 'категории продукта'

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'created', 'display_categories')
    list_filter = ('category', 'created')
    search_fields = ('title', 'category__title')
    inlines = [CategoryInline, ImagesProductInline, CharacteristicInline]
    exclude = ('category',)
    

    def display_categories(self, obj):
        return ', '.join(category.title for category in obj.category.all())

    display_categories.short_description = 'Категории продукта'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    search_fields = ('title', 'slug')
