from django.shortcuts import redirect
from django.views.generic import *
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login, mixins
from .forms import *
from .utils import *
from .services.products import *


class IndexView(TemplateView):
    """Представление главной страницы"""
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная'
        return context


class ShopView(ShopMixin, ListView):
    """Представление страницы магазина"""
    model = ProductsModel
    template_name = 'main/products.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        shop_context = self.get_shop_context(title='Товары')
        return context | shop_context


class CategoryView(ShopMixin, ListView):
    """Представление страницы магазина по категориям"""
    model = ProductsModel
    template_name = 'main/products.html'
    context_object_name = 'products'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        category = CategoryProductModel.objects.get(slug=self.kwargs['category_slug'])
        shop_context = self.get_shop_context(title=category.name, active=category.pk)
        return context | shop_context

    def get_queryset(self):
        return ProductsModel.objects.filter(category__slug=self.kwargs['category_slug'])


class ProductView(DetailView):
    """Представление отдельного продукта"""
    model = ProductsModel
    template_name = 'main/product.html'
    pk_url_kwarg = 'product_id'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = ProductsModel.objects.get(pk=self.kwargs['product_id']).name
        return context


class AddProductView(mixins.LoginRequiredMixin, CreateView):
    """Отображение страницы добавления продуктов"""
    form_class = AddProductForm
    template_name = 'main/add_product.html'
    success_url = reverse_lazy('home')
    login_url = 'sign_in'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление продукта'
        return context


class CartView(mixins.LoginRequiredMixin, ListView):
    """Отображение страницы корзины"""
    model = CartModel
    template_name = 'main/cart.html'
    context_object_name = 'products'
    login_url = reverse_lazy('sign_in')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Корзина'
        return context

    def get_queryset(self):
        return get_products_from_user_pk(self.request.user.pk)

    def get(self, request, *args, **kwargs):
        if request.GET and 'user' in request.GET and 'product' in request.GET:
            del_product_to_cart(request.GET['user'], request.GET['product'])
        return super().get(request, *args, **kwargs)


class RegistrationView(CreateView):
    """Отображение страницы входа/регистрации"""
    form_class = AddUserForm
    template_name = 'main/sign_in.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        context['url_action'] = 'registration'
        context['active'] = 1
        context['btn_text'] = 'Зарегистрироваться'
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class SingInView(LoginView):
    form_class = LoginUserForm
    template_name = 'main/sign_in.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Вход'
        context['url_action'] = 'sign_in'
        context['active'] = 0
        context['btn_text'] = 'Войти'
        return context

    def form_valid(self, form):
        login(self.request, form.get_user())
        return redirect('profile')


class ProfileView(mixins.LoginRequiredMixin, DetailView):
    model = UsersModel
    template_name = 'main/user.html'
    slug_url_kwarg = 'username_slug'
    context_object_name = 'user'
    login_url = 'sign_in'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.request.user.username
        return context

    def get_object(self, queryset=None):
        return UsersModel.objects.get(username=self.request.user.username)


def sign_out_view(request):
    logout(request)
    return redirect('sign_in')
