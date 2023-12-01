# Generated by Django 4.2.7 on 2023-11-29 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_remove_settings_image_banner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clients', models.CharField(default='0', max_length=155, verbose_name='Счастливые клиенты')),
                ('employees', models.CharField(default='0', max_length=155, verbose_name='кол-во сотрудников')),
                ('orders', models.CharField(default='0', max_length=155, verbose_name='кол-во заказов в месяц')),
                ('products', models.CharField(default='0', max_length=155, verbose_name='кол-во продуктов')),
            ],
            options={
                'verbose_name': 'Наша статистика',
                'verbose_name_plural': 'Наша статистика',
            },
        ),
    ]