from django.contrib import admin
from .models import *


class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'username', 'email', 'photo', 'money')
    list_display_links = ('first_name', 'last_name', 'username', 'money')
    search_fields = ('first_name', 'last_name', 'username', 'email')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'photo', 'price', 'category_id')
    list_display_links = ('name', 'description', 'price', 'category_id')
    search_fields = ('description', 'price', 'category_id')


class CategoryProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('name', 'slug')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_id', 'user_id')
    search_fields = ('product_id', 'user_id')


admin.site.register(UsersModel, UsersAdmin)
admin.site.register(ProductsModel, ProductAdmin)
admin.site.register(CategoryProductModel, CategoryProductAdmin)
admin.site.register(CartModel, CartAdmin)
