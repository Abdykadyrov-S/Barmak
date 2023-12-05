from django.db import models
from apps.users.models import User

# Create your models here.
class Category(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    slug = models.SlugField(
        verbose_name="Slug"
    )
    image = models.ImageField(
        max_length=1000,
        upload_to='category/',
        verbose_name="Фотография категории",
        default='no_image.jpg'
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Brand(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название бренда"
    )
    slug = models.SlugField(
        verbose_name="Slug"
    )
    image = models.ImageField(
        max_length=1000,
        upload_to='brand/',
        verbose_name="Фотография категории",
        default='no_image.jpg'
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Бренд продукта"
        verbose_name_plural = "Бренды продуктов"

class Product(models.Model):
    category = models.ManyToManyField(
        Category,
        related_name="category_products",
        verbose_name="Категории"
    )
    brand = models.ForeignKey(
        Brand, on_delete=models.SET_NULL,
        related_name="brand_products",
        blank=True, null=True
    )
    title = models.CharField(
        max_length=300,
        verbose_name="Название"
    )
    description = models.TextField(
        verbose_name="Короткое описание",
        blank=True, null=True
    )
    popular = models.BooleanField(
        default=False, 
        verbose_name="Товар популярный (трендовый)?"
    )
    product_day = models.BooleanField(
        default=False, 
        verbose_name="Товар дня"
    )
    new = models.BooleanField(
        default=False, 
        verbose_name="Товар новый (Новые поступления)?"
    )
    featured = models.BooleanField(
        default=False, 
        verbose_name="Рекомендуемые продукты"
    )
    sale = models.BooleanField(
        default=False,
        verbose_name="Распродажа"
    )
    price = models.CharField(
        max_length=100,
        verbose_name="Цена"
    )
    old_price = models.CharField(
        max_length=100,
        verbose_name="Старая цена",
        blank=True, null=True
    )
    image = models.ImageField(
        max_length=1000,
        upload_to='product/',
        verbose_name="Фотография продукта",
        default='no_image.jpg'
    )
    image_2 = models.ImageField(
        max_length=1000,
        upload_to='product/',
        verbose_name="Фотография продукта №2 (Другая расцветка или другой ракурс)",
        default='no_image.jpg'
    )
    image_3 = models.ImageField(
        max_length=1000,
        upload_to='product/',
        verbose_name="Фотография продукта №3 (Другая расцветка или другой ракурс)",
        default='no_image.jpg'
    )
    image_4 = models.ImageField(
        max_length=1000,
        upload_to='product/',
        verbose_name="Фотография продукта №4 (Другая расцветка или другой ракурс)",
        default='no_image.jpg'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    title_2 = models.CharField(
        max_length=300,
        verbose_name="заголовок для описания",
        blank=True, null=True
    )
    description_2 = models.TextField(
        verbose_name="Подробное описание",
        blank=True, null=True
    )
    about_product_image = models.ImageField(
        max_length=1000,
        upload_to='product/',
        verbose_name="Фотография продукта для описания",
        default='no_image.jpg'
    )
    
    def get_characteristics(self):
        return self.characteristics.all()

    def __str__(self):
        return self.title 
    
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

class Characteristic(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        related_name="characteristics",
        verbose_name="Товар"
    )
    name = models.CharField(
        max_length=300,
        verbose_name="Название характеристики"
    )
    value = models.CharField(
        max_length=300,
        verbose_name="Значение характеристики"
    )

    def __str__(self):
        return f"{self.product.title} - {self.name}"

    class Meta:
        verbose_name = "Характеристика"
        verbose_name_plural = "Характеристики"


class ReviewProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL,
        related_name="review_product",
        blank=True, null=True
    )
    message = models.TextField(
        verbose_name="Текст отзыва",
        null=True,blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.BooleanField(
        verbose_name="Выложить на сайт",
        default=False
    )
    def __str__(self):
        return f"Отзыв для продукта {self.product}"

    class Meta:
        verbose_name = "Отзыв продукта"
        verbose_name_plural = "Отзывы продуктов"
