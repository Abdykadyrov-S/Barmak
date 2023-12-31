# Generated by Django 4.2.7 on 2023-12-05 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_delete_productcomparison'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название бренда')),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('image', models.ImageField(default='no_image.jpg', max_length=1000, upload_to='brand/', verbose_name='Фотография категории')),
            ],
            options={
                'verbose_name': 'Бренд продукта',
                'verbose_name_plural': 'Бренды продуктов',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='brand_products', to='products.brand'),
        ),
    ]
