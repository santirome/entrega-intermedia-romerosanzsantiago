from django.contrib import admin
from products.models import Products, Category

admin.site.index_template = "/index.html"
admin.site.register(Products)
admin.site.register(Category)