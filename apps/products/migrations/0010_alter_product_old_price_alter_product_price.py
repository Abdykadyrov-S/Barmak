# Generated by Django 4.2.7 on 2023-11-29 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_product_old_price_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='old_price',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Старая цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(max_length=100, verbose_name='Цена'),
        ),
    ]
