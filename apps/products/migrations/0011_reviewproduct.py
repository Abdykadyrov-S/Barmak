# Generated by Django 4.2.7 on 2023-11-29 15:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0010_alter_product_old_price_alter_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(blank=True, null=True, verbose_name='Текст отзыва')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('post', models.BooleanField(verbose_name='Выложить на сайт')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='review_product', to='products.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Отзыв продукта',
                'verbose_name_plural': 'Отзывы продуктов',
            },
        ),
    ]
