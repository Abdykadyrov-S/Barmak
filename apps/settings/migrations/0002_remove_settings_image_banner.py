# Generated by Django 4.2.7 on 2023-11-27 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='settings',
            name='image_banner',
        ),
    ]
