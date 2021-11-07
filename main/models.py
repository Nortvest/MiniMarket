from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


class UsersModel(AbstractUser):
    """Таблица пользователей"""
    photo = models.ImageField(upload_to="users/%Y/%m/%d", blank=True, verbose_name="Путь до фото пользователя")
    money = models.IntegerField(verbose_name="Кол-во денег", default=0)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Данные пользователя'
        verbose_name_plural = 'Данные пользователей'


class ProductsModel(models.Model):
    """Таблица продуктов"""
    name = models.CharField(max_length=255, verbose_name="Наименование товара")
    description = models.TextField(blank=True, verbose_name="Описание товара")
    photo = models.ImageField(upload_to="photo/%Y/%m/%d", blank=True, verbose_name="Путь до фото товара")
    price = models.IntegerField(verbose_name="Цена товара")
    category = models.ForeignKey(to="CategoryProductModel", on_delete=models.PROTECT, verbose_name="Категория товара")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product', kwargs={'category_slug': CategoryProductModel.objects.get(name=self.category).slug,
                                          'product_id': self.pk})

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class CategoryProductModel(models.Model):
    """Таблица категорий продуктов"""
    name = models.CharField(max_length=255, verbose_name="Название категории")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_products', kwargs={'category_slug': self.slug})

    class Meta:
        verbose_name = 'Категория продуктов'
        verbose_name_plural = 'Категории продуктов'


class CartModel(models.Model):
    """Таблица корзины"""
    user = models.ForeignKey(to=UsersModel, on_delete=models.PROTECT, verbose_name="id пользователя")
    product = models.ForeignKey(to=ProductsModel, on_delete=models.PROTECT, verbose_name="id продукта")

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
