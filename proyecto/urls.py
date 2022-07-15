from django.contrib import admin
from django.urls import path, include
from proyecto.views import fecha_actual, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fecha_actual/', fecha_actual, name = 'fecha_actual'),
    path('familia/', include('familia.urls')),
    path('', index, name = 'index'),
    path('products/', include('products.urls')),
]
