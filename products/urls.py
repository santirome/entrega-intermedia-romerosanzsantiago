from django.urls import path, include
from products.views import create_product_view, products, contacto, search_product_view, create_category_view, create_discount_view
from django.contrib import admin
from proyecto.views import index
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('', products, name = 'products'),
    path('contacto/', contacto, name = 'contacto'),
    path('create-product/', create_product_view, name = 'create-product'),
    path('search-product/', search_product_view, name = 'search_product_view'),
    path('create-category/', create_category_view, name = 'create-category'),
    path('create-discount/', create_discount_view, name = 'create-discount'),

]


