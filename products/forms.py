from django import forms

class Product_form(forms.Form):
    name = forms.CharField(label="Nombre", max_length=40)
    price = forms.FloatField(label="Precio", widget=forms.NumberInput(attrs={'placeholder': "En números"}))
    description = forms.CharField(label="Descripción", max_length=200)
    SKU = forms.CharField(label="ID", max_length=30)
    active = forms.BooleanField()

class Category_form(forms.Form):
    name = forms.CharField(label="Nombre", max_length=40)
    description = forms.CharField(label="Descripción", max_length=200)

class Discount_form(forms.Form):
    name = forms.CharField(label="Nombre", max_length=40)
    description = forms.CharField(label="Descripción", max_length=40)