from django.http import HttpResponse
from django.shortcuts import render

from .models import Articulos, Empleados, Proveedores, Clientes, Compras , compraProd, Ventas

def index(request):
    return render(request, 'index.html')

def contador(request):
    mensaje = f"<html><h2> Bienvenidos al sistema Rie Victoria</h2>"\
    f"<p> Este es un sistema de control de stock</p></html>"\
    f"<p>En el sistema hay {Articulos.objects.count()}articulos cargados</p></html>"\
    f"<p>En el sistema hay {Clientes.objects.count ()}clientes cargados.</p><html>"
    return HttpResponse(mensaje)

#DE PRUEBA
def bienvenida(request):
    #un nombre con el que llamo a la variable : modelo objeto que voy a mandar
    context = {'Articulos': Articulos.objects.all()}
    {'Clientes': Clientes.objects.all()}
    #template, el render manda el contexto al template||
    return render(request, 'bienvenida.html', context)


def tabla(request):
    #un nombre con el que llamo a la variable : modelo objeto que voy a mandar
    context = {'Articulos': Articulos.objects.all()}
     #template, el render manda el contexto al template||
    return render(request, 'tabla.html', context)

#pk es la referencia al id del articulo
def articulos(request, pk):
    art = Articulos.objects.get(id=pk)
    #un nombre con el que llamo a la variable : modelo objeto que voy a mandar
    context = {'art': art}
    #template, el render manda el contexto al template||
    return render(request, 'articulos.html', context)

def tablaclientes (request):
    context= {'Clientes': Clientes.objects.all()}
    return render (request, 'tablaclientes.html', context)

def clientes(request,pk):
    #un nombre con el que llamo a la variable : modelo objeto que voy a mandar
    cli =Clientes.objects.get(id=pk)
    context =  {'cli' : cli}
    #{'Clientes': Clientes.objects.all()}
    #template, el render manda el contexto al template||
    return render(request, 'clientes.html', context)

def tablaempleados(request):
    context = {'Empleados': Empleados.objects.all()}
    return render (request, 'tablaempleados.html', context)

def empleados(request, pk):
    #un nombre con el que llamo a la variable : modelo objeto que voy a mandar}
    empl = Empleados.objects.get(id=pk)
    context = {'empl': empl}
    #template, el render manda el contexto al template||
    return render(request, 'empleados.html', context)

def proveedores(request, pk):
    prov = Proveedores.objects.get(id=pk)
    #un nombre con el que llamo a la variable : modelo objeto que voy a mandar
    context = {'prov': prov}
    #template, el render manda el contexto al template||
    return render(request, 'proveedores.html', context)

def tablaproveedores (request):
    context= {'Proveedores': Proveedores.objects.all()}
    return render (request, 'tablaproveedores.html', context)

def tablaCompras(request):
    #un nombre con el que llamo a la variable : modelo objeto que voy a mandar
    context = {'Compras': Compras.objects.all()}
     #template, el render manda el contexto al template||
    return render(request, 'tablaCompras.html', context)

#pk es la referencia al id del articulo
def compras(request, pk):
    com = Compras.objects.get(id=pk)
    arts = compraProd.objects.filter(idCompra_id=pk)
    #un nombre con el que llamo a la variable : modelo objeto que voy a mandar
    context = {'com': com, 'arts':arts}
    #template, el render manda el contexto al template||
    return render(request, 'compras.html', context)

def tablaVentas(request):
    #un nombre con el que llamo a la variable : modelo objeto que voy a mandar
    context = {'Ventas': Ventas.objects.all()}
     #template, el render manda el contexto al template||
    return render(request, 'tablaVentas.html', context)

# #pk es la referencia al id del articulo
# def compras(request, pk):
#     com = Compras.objects.get(id=pk)
#     arts = compraProd.objects.filter(idCompra_id=pk)
#     #un nombre con el que llamo a la variable : modelo objeto que voy a mandar
#     context = {'com': com, 'arts':arts}
#     #template, el render manda el contexto al template||
#     return render(request, 'compras.html', context)