from django.http import HttpResponse
from django.shortcuts import render

from .models import Articulos, Empleados, Proveedores

def index(request):
    mensaje = f"<html><h2> Bienvenidos al sistema Rie Victoria</h2>"\
    f"<p> Este es un sistema de control de stock</p></html>"
    return HttpResponse(mensaje)

def contador(request):
    mensaje = f"<html><h2> Bienvenidos al sistema Rie Victoria</h2>"\
    f"<p> Este es un sistema de control de stock</p></html>"\
    f"<p>En el sistema hay {Articulos.objects.count()}articulos cargados</p></html>"
    return HttpResponse(mensaje)

def bienvenida(request):
    #un nombre con el que llamo a la variable : modelo objeto que voy a mandar                                 
    context = {'Articulos': Articulos.objects.all()}
    #template, el render manda el contexto al template||
    return render(request, 'bienvenida.html', context)

def tabla(request):
    #un nombre con el que llamo a la variable : modelo objeto que voy a mandar                                 
    context = {'Articulos': Articulos.objects.all()}
    #template, el render manda el contexto al template||
    return render(request, 'tabla.html', context)
    