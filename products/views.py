from django import forms
from django.http import HttpResponse
from django.shortcuts import render
from products.models import Discount, Products , Category
from products.forms import Product_form, Category_form, Discount_form
from django.http import HttpResponse


def products(request):
    productos =  Products.objects.all()
    context = {'productos':productos}
    return render(request, 'products.html', context=context)

def contacto(request):
    return render(request, 'contacto.html')

def create_product_view(request):
    if request.method == 'GET':
        form = Product_form()
        context = {'form':form}
        return render(request, 'create_product.html', context=context)
    else:
        form = Product_form(request.POST)
        if form.is_valid():
            new_product = Products.objects.create(
                name = form.cleaned_data['name'],
                price = form.cleaned_data['price'],
                description = form.cleaned_data['description'],
                SKU = form.cleaned_data['SKU'],
                active = form.cleaned_data['active'],
            )
            context = {'new_product':new_product}
        return HttpResponse('Viniste por POST')

def search_product_view(request):
    print(request.GET)
    products = Products.objects.filter(name__icontains = request.GET['Search'])
    context = {'products':products}
    return render(request, 'search_product.html', context = context)

def create_category_view(request):
    if request.method == 'GET':
        form = Category_form()
        context = {'form':form}
        return render(request, 'create_category.html', context=context)
    else:
        form = Category_form(request.POST)
        if form.is_valid():
            new_category = Category.objects.create(
                name = form.cleaned_data['name'],
                description = form.cleaned_data['description'],
                active = form.cleaned_data['active'],
            )
            context = {'new_category':new_category}
        return HttpResponse('Viniste por POST')

def search_category_view(request):
    print(request.GET)
    category = Category.objects.filter(name__icontains = request.GET['Search'])
    context = {'category':category}
    return render(request, 'search_category.html', context = context)

def create_discount_view(request):
    if request.method == 'GET':
        form = Discount_form()
        context = {'form':form}
        return render(request, 'create_discount.html', context=context)
    else:
        form = Discount_form(request.POST)
        if form.is_valid():
            new_discount = Discount.objects.create(
                name = form.cleaned_data['name'],
                description = form.cleaned_data['description'],
                price = form.cleaned_data['price'],
                active = form.cleaned_data['active'],
            )
            context = {'new_discount':new_discount}
        return HttpResponse('Viniste por POST')

def search_discounts_view(request):
    print(request.GET)
    discount = Discount.objects.filter(name__icontains = request.GET['Search'])
    context = {'discount':discount}
    return render(request, 'search_discount.html', context = context)

def no_hay_error(request):
    return HttpResponse('No hay error, usted se tiene que arrepentir de lo que dijo.')