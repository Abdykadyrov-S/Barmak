# Generated by Django 4.2.7 on 2023-11-27 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_key', models.CharField(max_length=40, unique=True, verbose_name='Ключ сессии')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания корзины')),
            ],
            options={
                'verbose_name': 'Корзина',
                'verbose_name_plural': 'Корзины',
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Количество товара')),
                ('total', models.PositiveBigIntegerField(default=0, verbose_name='Итоговая цена товаров')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carts.cart', verbose_name='Корзина')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Товар в корзине',
                'verbose_name_plural': 'Товары в корзине',
            },
        ),
        migrations.AddField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(through='carts.CartItem', to='products.product', verbose_name='Товары'),
        ),
    ]
