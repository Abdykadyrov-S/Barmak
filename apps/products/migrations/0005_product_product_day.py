# Generated by Django 4.2.7 on 2023-11-27 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_remove_product_is_popular_product_discount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_day',
            field=models.BooleanField(default=False, verbose_name='Товар дня'),
        ),
    ]
