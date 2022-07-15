from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def fecha_actual(request):
    fecha = datetime.now().date()
    mensaje = f"Hoy es {fecha}"
    return HttpResponse(mensaje)

def index(request):
    return render(request, 'index.html')
