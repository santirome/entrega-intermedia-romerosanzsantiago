from django.contrib import admin
from django.urls import path, include
from proyecto.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'index'),
    path('products/', include('products.urls')),
]
