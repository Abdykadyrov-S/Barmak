# Generated by Django 4.2.7 on 2023-11-27 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_product_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='about_product_image',
            field=models.ImageField(default='no_image.jpg', max_length=1000, upload_to='', verbose_name='Фотография продукта для описания'),
        ),
        migrations.AddField(
            model_name='product',
            name='description_3',
            field=models.TextField(blank=True, null=True, verbose_name='Подробное описание'),
        ),
        migrations.AddField(
            model_name='product',
            name='title_2',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='заголовок для описания'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Короткое описание'),
        ),
    ]