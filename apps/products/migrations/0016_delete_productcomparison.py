# Generated by Django 4.2.7 on 2023-12-03 00:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_rename_comparisonlist_productcomparison'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductComparison',
        ),
    ]
