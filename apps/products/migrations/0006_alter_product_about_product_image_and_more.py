# Generated by Django 4.2.7 on 2023-11-29 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_characteristic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='about_product_image',
            field=models.ImageField(default='no_image.jpg', max_length=1000, upload_to='product/', verbose_name='Фотография продукта для описания'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='no_image.jpg', max_length=1000, upload_to='product/', verbose_name='Фотография продукта'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_2',
            field=models.ImageField(default='no_image.jpg', max_length=1000, upload_to='product/', verbose_name='Фотография продукта №2 (Другая расцветка или другой ракурс)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_3',
            field=models.ImageField(default='no_image.jpg', max_length=1000, upload_to='product/', verbose_name='Фотография продукта №3 (Другая расцветка или другой ракурс)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_4',
            field=models.ImageField(default='no_image.jpg', max_length=1000, upload_to='product/', verbose_name='Фотография продукта №4 (Другая расцветка или другой ракурс)'),
        ),
    ]
