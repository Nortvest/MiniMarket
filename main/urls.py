from django.urls import path, include
from .views import *
from Market import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('products/', ShopView.as_view(), name='products'),
    path('products/<slug:category_slug>/', CategoryView.as_view(), name='category_products'),
    path('products/<slug:category_slug>/<int:product_id>', ProductView.as_view(), name='product'),
    path('add_product/', AddProductView.as_view(), name='add_product'),
    path('cart/', CartView.as_view(), name='cart'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('sign_in/', SingInView.as_view(), name='sign_in'),
    path('sign_out/', sign_out_view, name='sign_out'),
    path('registration/', RegistrationView.as_view(), name='registration')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
