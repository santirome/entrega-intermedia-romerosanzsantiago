from enum import unique
from django.db import models
from django.forms import IntegerField

class Products(models.Model):
    name = models.CharField(max_length=40)
    price = models.IntegerField()
    description = models.CharField(max_length=200, blank=True, null=True)
    SKU = models.CharField(max_length=30, unique=True, error_messages={"unique":"This email has already been registered."})

    def __str__(self):
        return f"Producto: {self.name} - Precio: {self.price} - Descripción: {self.description}"
    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
            

class Category(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=100)


    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

class Discount(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=100)


    class Meta:
        verbose_name = 'descuento'
        verbose_name_plural = 'descuentos'


