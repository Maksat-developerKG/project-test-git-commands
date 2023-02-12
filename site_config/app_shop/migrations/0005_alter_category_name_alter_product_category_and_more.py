# Generated by Django 4.1.6 on 2023-02-12 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_shop', '0004_alter_product_sub_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(blank=True, max_length=100, verbose_name='Категория:'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(blank=True, to='app_shop.category', verbose_name='Категория:'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sub_category',
            field=models.ManyToManyField(blank=True, to='app_shop.subcategory', verbose_name='Под категория'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='name',
            field=models.CharField(blank=True, max_length=100, verbose_name='Под категория:'),
        ),
    ]