# Generated by Django 4.0.4 on 2022-06-12 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'categoria', 'verbose_name_plural': 'categorias'},
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name': 'producto', 'verbose_name_plural': 'productos'},
        ),
    ]
