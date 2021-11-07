from .models import *
from .services.products import *


class ShopMixin:
    """Mixin-класс для страниц магазина"""
    paginate_by = 4

    def get_shop_context(self, **kwargs):
        context = kwargs
        context['menu'] = CategoryProductModel.objects.all()
        context['product_in_cart'] = get_products_from_user_pk(self.request.user.pk)
        if 'active' not in context:
            context['active'] = 0
        return context

    def get(self, request, *args, **kwargs):
        if request.GET and 'user' in request.GET and 'product' in request.GET:
            add_product_to_cart(request.GET['user'], request.GET['product'])
        return super().get(request, *args, **kwargs)
