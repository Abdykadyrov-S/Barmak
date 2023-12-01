# Generated by Django 4.2.7 on 2023-11-30 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_alter_reviewproduct_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(related_name='category_products', to='products.category', verbose_name='Категории'),
        ),
    ]