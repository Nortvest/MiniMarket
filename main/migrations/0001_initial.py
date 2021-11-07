# Generated by Django 3.2.8 on 2021-10-31 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название категории')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категория продуктов',
                'verbose_name_plural': 'Категории продуктов',
            },
        ),
        migrations.CreateModel(
            name='UsersModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255, verbose_name='Имя')),
                ('lastname', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('username', models.CharField(max_length=255, unique=True, verbose_name='Ник')),
                ('password', models.CharField(max_length=1024, verbose_name='Пароль')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('photo', models.ImageField(blank=True, upload_to='users/%Y/%m/%d', verbose_name='Путь до фото пользователя')),
                ('money', models.IntegerField(default=0, verbose_name='Кол-во денег')),
            ],
            options={
                'verbose_name': 'Данные пользователя',
                'verbose_name_plural': 'Данные пользователей',
            },
        ),
        migrations.CreateModel(
            name='ProductsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование товара')),
                ('description', models.TextField(blank=True, verbose_name='Описание товара')),
                ('photo', models.ImageField(blank=True, upload_to='photo/%Y/%m/%d', verbose_name='Путь до фото товара')),
                ('price', models.IntegerField(verbose_name='Цена товара')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.categoryproductmodel', verbose_name='Категория товара')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='CartModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.productsmodel', verbose_name='id продукта')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.usersmodel', verbose_name='id пользователя')),
            ],
            options={
                'verbose_name': 'Корзина',
                'verbose_name_plural': 'Корзины',
            },
        ),
    ]