from ..models import *


def add_product_to_cart(user_id, product_id):
    """Добавление в корзину"""
    if not CartModel.objects.filter(product_id=product_id, user_id=user_id).count():
        CartModel(product_id=product_id, user_id=user_id).save()


def del_product_to_cart(user_id, product_id):
    """Удаление из корзины"""
    if CartModel.objects.filter(product_id=product_id, user_id=user_id).count():
        CartModel.objects.get(product_id=product_id, user_id=user_id).delete()


def get_products_from_user_pk(user_pk):
    products = [i.product_id for i in CartModel.objects.filter(user_id=user_pk)]
    return ProductsModel.objects.filter(pk__in=products)
