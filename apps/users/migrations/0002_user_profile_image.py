# Generated by Django 4.2.7 on 2023-11-29 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank=True, default='profile_image/no_image.png', null=True, upload_to='profile_image/', verbose_name='Фотография профиля'),
        ),
    ]
