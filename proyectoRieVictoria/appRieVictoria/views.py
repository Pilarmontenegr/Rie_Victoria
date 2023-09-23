from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render
from django.urls import reverse ,reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Articulos, Empleados, Proveedores, Clientes, Compras , compraProd, Ventas, ventaProd
from .forms import ProveedoresForm , EmpleadosForm , ClientesForm , ArticulosForm ,ventaProdForm , VentasForm, ventasFormset
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


#pk es la referencia al id del articulo
def articulos(request, pk):
    art = Articulos.objects.get(id=pk)
    #un nombre con el que llamo a la variable : modelo objeto que voy a mandar
    context = {'art': art}
    #template, el render manda el contexto al template||
    return render(request, 'articulos.html', context)

def tabla(request):
    #un nombre con el que llamo a la variable : modelo objeto que voy a mandar
    context = {'Articulos': Articulos.objects.all()}
     #template, el render manda el contexto al template||
    return render(request, 'tabla.html', context)

# #ARTICULOS ESTÁ HECHO EN VISTA BASADA EN CLASES -----------------------------------------------
# class Tabla(ListView):
#     model = Articulos
#     template_name = 'tabla.html'
#     context_object_name = 'articulos'

# class ArticulosNuevo (CreateView):
#     model = Articulos
#     form_class = ArticulosForm
#     template_name = 'articulosForm.html'
#     success_url = reverse_lazy('tabla.html')

# class ArticulosModif(UpdateView):
#     model = Articulos
#     form_class = ArticulosForm
#     template_name = 'articulosForm.html'
#     success_url = reverse_lazy('tabla.html')

# class ArticulosBorrar(DeleteView):
#     model = Articulos
#     template_name = 'articulosConfBorrar.html'
#     success_url = reverse_lazy('tabla.html')



def ArticulosModif(request, pk):
    articulos = Articulos.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticulosForm(request.POST, instance=articulos)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tabla'))
    else:
        form = ArticulosForm(instance=articulos)
    return render(request, 'ArticulosForm.html', {'form': form, 'articulos': articulos})


def ArticulosNuevo(request):
    if request.method == 'POST':
        form = ArticulosForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tabla'))
    else:
        form = ArticulosForm()
    return render(request, 'ArticulosForm.html', {'form': form})


def ArticulosBorrar(request, pk):
    articulos = Articulos.objects.get(pk=pk)
    if request.method == 'POST':
        articulos.delete()
        return HttpResponseRedirect(reverse('tabla'))
    return render(request, 'ArticulosConfBorrar.html', {'articulos': articulos})







#este es de las chicas

# def ArticulosLista(request):
#     articulos = Articulos.objects.all()
#     context = {"articulos": articulos}
#     return render(request, "articulosLista.html", context)
# def ArticulosModif(request, pk):
#     Articulos = Articulos.objects.get(descripcion=pk)
#     if request.method == 'POST':
#         descripcion = request.POST.get('descripcion')
#         costo = request.POST.get('costo')
#         venta = request.POST.get('venta')
#         cantidad = request.POST.get('cantidad')
#         talle = request.POST.get('talle')
#         tipoPrenda= request.POST.get('tipoPrenda')
#         articulos.descripcion = descripcion
#         articulos.costo = costo
#         articulos.venta = venta
#         articulos.cantidad= cantidad
#         articulos.talle = talle
#         articulos.tipoPrenda = tipoPrenda
       
#         return HttpResponseRedirect(reverse('articulosLista'))
#     return render(request, "articulosForm.html", {'articulos': articulos})


# def ArticulosNuevo(request):
#     if request.method == 'POST':
#         descripcion = request.POST.get('descripcion')
#         costo = request.POST.get('costo')
#         venta = request.POST.get('venta')
#         cantidad = request.POST.get('cantidad')
#         talle = request.POST.get('talle')
#         tipoPrenda = request.POST.get('tipoPrenda')
#         Articulos.objects.create(descripcion=descripcion, costo=costo, cantidad=cantidad, venta=venta, \
#                                  talle = talle, tipoPrenda=tipoPrenda)
#         return HttpResponseRedirect(reverse('articulosLista'))
#     return render(request, "articulos.html")


# def ArticulosBorrar(request, pk):
#     Articulos = Articulos.objects.get(descripcion=pk)
#     if request.method == 'POST':
#         articulos.delete()
#         return HttpResponseRedirect(reverse('articulosLista'))
#     return render(request, 'articulosConfBorrar.html', {'articulos': articulos})








# def ClientesModif(request, pk):
#     clientes = Clientes.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = ClientesForm(request.POST, instance=clientes)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('tablaclientes'))
#     else:
#         form = ClientesForm(instance=clientes)
#     return render(request, 'ClientesForm.html', {'form': form, 'clientes': clientes})


# def ClientesNuevo(request):
#     if request.method == 'POST':
#         form = ClientesForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('tablaclientes'))
#     else:
#         form = ClientesForm()
#     return render(request, 'ClientesForm.html', {'form': form})


# def ClientesBorrar(request, pk):
#     clientes = Clientes.objects.get(pk=pk)
#     if request.method == 'POST':
#         clientes.delete()
#         return HttpResponseRedirect(reverse('tablaclientes'))
#     return render(request, 'ClientesConfBorrar.html', {'clientes': clientes})
def clientes(request,pk):
    #un nombre con el que llamo a la variable : modelo objeto que voy a mandar
    cli =Clientes.objects.get(id=pk)
    context =  {'cli' : cli}
    #{'Clientes': Clientes.objects.all()}
    #template, el render manda el contexto al template||
    return render(request, 'clientes.html', context)


# def tablaclientes (request):
#     context= {'Clientes': Clientes.objects.all()}
#     return render (request, 'tablaclientes.html', context)

class TablaClientes(ListView):
    model = Clientes
    template_name = 'tablaclientes.html'
    context_object_name = 'Clientes'


class ClientesNuevo(CreateView):
    model = Clientes
    form_class = ClientesForm
    template_name = 'clientesForm.html'
    success_url = reverse_lazy('tablaclientes')


class ClientesModif(UpdateView):
    model = Clientes
    form_class = ClientesForm
    template_name = 'clientesForm.html'
    success_url = reverse_lazy('tablaclientes')


class ClientesBorrar(DeleteView):
    model = Clientes
    template_name = 'ClientesConfBorrar.html'
    success_url = reverse_lazy('tablaclientes')



def tablaempleados(request):
    context = {'Empleados': Empleados.objects.all()}
    return render (request, 'tablaempleados.html', context)


def empleados(request, pk):
    #un nombre con el que llamo a la variable : modelo objeto que voy a mandar}
    empl = Empleados.objects.get(id=pk)
    context = {'empl': empl}
    #template, el render manda el contexto al template||
    return render(request, 'empleados.html', context)

def EmpleadosModif(request, pk):
    empleados = Empleados.objects.get(pk=pk)
    if request.method == 'POST':
        form = EmpleadosForm(request.POST, instance=empleados)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tablaempleados'))
    else:
        form = EmpleadosForm(instance=empleados)
    return render(request, 'EmpleadosForm.html', {'form': form, 'empleados': empleados})


def EmpleadosNuevo(request):
    if request.method == 'POST':
        form = EmpleadosForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tablaempleados'))
    else:
        form = EmpleadosForm()
    return render(request, 'EmpleadosForm.html', {'form': form})


def EmpleadosBorrar(request, pk):
    empleados = Empleados.objects.get(pk=pk)
    if request.method == 'POST':
        empleados.delete()
        return HttpResponseRedirect(reverse('tablaempleados'))
    return render(request, 'empleadosConfBorrar.html', {'empleados': empleados})



def proveedores(request, pk):
    prov = Proveedores.objects.get(id=pk)
    #un nombre con el que llamo a la variable : modelo objeto que voy a mandar
    context = {'prov': prov}
    #template, el render manda el contexto al template||
    return render(request, 'proveedores.html', context)

def ProveedoresModif(request, pk):
    proveedores = Proveedores.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProveedoresForm(request.POST, instance=proveedores)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tablaproveedores'))
    else:
        form = ProveedoresForm(instance=proveedores)
    return render(request, 'ProveedoresForm.html', {'form': form, 'proveedores': proveedores})


def ProveedoresNuevo(request):
    if request.method == 'POST':
        form = ProveedoresForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tablaproveedores'))
    else:
        form = ProveedoresForm()
    return render(request, 'ProveedoresForm.html', {'form': form})


def ProveedoresBorrar(request, pk):
    proveedores = Proveedores.objects.get(pk=pk)
    if request.method == 'POST':
        proveedores.delete()
        return HttpResponseRedirect(reverse('tablaproveedores'))
    return render(request, 'proveedoresConfBorrar.html', {'proveedores': proveedores})


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






# def tablaVentas(request):
#     #un nombre con el que llamo a la variable : modelo objeto que voy a mandar
#     context = {'Ventas': Ventas.objects.all()}
#      #template, el render manda el contexto al template||
#     return render(request, 'tablaVentas.html', context)


#pk es la referencia al id del articulo
def ventas(request, pk):
    ven = Ventas.objects.get(id=pk)
    ventProd = ventaProd.objects.filter(idVenta_id=pk)
    #un nombre con el que llamo a la variable : modelo objeto que voy a mandar
    context = {'ven': ven, 'ventProd':ventProd}
    #template, el render manda el contexto al template||
    return render(request, 'ventas.html', context)



class TablaVentas(ListView):
    model = Ventas
    template_name = 'tablaVentas.html'
    context_object_name = 'Ventas'
class VentasNuevo(CreateView):
    model = Ventas
    form_class = VentasForm
    template_name = 'VentasForm.html'
    success_url = reverse_lazy('tablaVentas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = VentasForm.ventasFormset(self.request.POST)
        else:
            context['formset'] = VentasForm.ventasFormset()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid() and form.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))


class VentasModif(UpdateView):
    model = Ventas
    form_class = VentasForm
    template_name = 'VentasForm.html'
    success_url = reverse_lazy('tablaVentas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = VentasForm.ventasFormset(self.request.POST, instance=self.object)
        else:
            context['formset'] = VentasForm.ventasFormset(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid() and form.is_valid():
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))
        
class VentasBorrar(DeleteView):
    model = Ventas
    template_name = 'ViajesConfBorrar.html'
    success_url = reverse_lazy('tablaVentas')