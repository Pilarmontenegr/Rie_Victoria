from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render, redirect
from django.urls import reverse ,reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Sum
from django.views import View
from datetime import datetime

from django.views.generic.list import ListView

from django.contrib.auth import logout
from django.contrib.auth.views import LoginView,LogoutView
from django.forms import inlineformset_factory

from django.contrib.auth.decorators import permission_required
from django.shortcuts import render


from django.http import HttpResponse

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4

from .models import Articulos, Empleados, Proveedores, Clientes, Compras , CompraProd, Ventas, VentaProd
from .forms import ProveedoresForm , EmpleadosForm , ClientesForm , ArticulosForm , VentasForm , ComprasForm
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

class tabla(ListView):
    model = Articulos
    template_name = 'tabla.html'
    context_object_name = 'Articulos'
    paginate_by = 8
    
    def get_queryset(self):
        query = self.request.GET.get('q', '')
        articulos = Articulos.objects.filter(descripcion__icontains=query)
        return articulos
    
    #para que se quede lo que busquemos 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q', '')
        context['query'] = query
        return context
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


def clientes(request,pk):
    #un nombre con el que llamo a la variable : modelo objeto que voy a mandar
    cli =Clientes.objects.get(id=pk)
    context =  {'cli' : cli}
    #{'Clientes': Clientes.objects.all()}
    #template, el render manda el contexto al template||
    return render(request, 'clientes.html', context)


class tablaClientes(ListView):
    model = Clientes
    template_name = 'tablaClientes.html'
    context_object_name = 'Clientes'
    paginate_by = 8
    
    def get_queryset(self):
        query = self.request.GET.get('q', '')
        clientes = Clientes.objects.filter(nombre__icontains=query)
        return clientes
    
    #para que se quede lo que busquemos 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q', '')
        context['query'] = query
        return context

def ClientesModif(request, pk):
    clientes = Clientes.objects.get(pk=pk)
    if request.method == 'POST':
        form = ClientesForm(request.POST, instance=clientes)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tablaclientes'))
    else:
        form = ClientesForm(instance=clientes)
    return render(request, 'ClientesForm.html', {'form': form, 'clientes': clientes})


def ClientesNuevo(request):
    if request.method == 'POST':
        form = ClientesForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tablaclientes'))
    else:
        form = ClientesForm()
    return render(request, 'ClientesForm.html', {'form': form})


def ClientesBorrar(request, pk):
    clientes = Clientes.objects.get(pk=pk)
    if request.method == 'POST':
        clientes.delete()
        return HttpResponseRedirect(reverse('tablaclientes'))
    return render(request, 'ClientesConfBorrar.html', {'clientes': clientes})


class tablaempleados(ListView):
    model = Empleados
    template_name = 'tablaempleados.html'
    context_object_name = 'Empleados'
    paginate_by = 8

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        empleados = Empleados.objects.filter(nombre__icontains=query)
        return empleados
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q', '')
        context['query'] = query
        return context
    
def empleados(request, pk):
    #un nombre con el que llamo a la variable : modelo objeto que voy a mandar}
    empl = Empleados.objects.get(id=pk)
    context = {'empl': empl}
    #template, el render manda el contexto al template||
    return render(request, 'empleados.html', context)

@permission_required('app.change_empleados', login_url='/login/')
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



class tablaproveedores(ListView):
    model = Proveedores
    template_name = 'tablaproveedores.html'
    context_object_name = 'Proveedores'
    paginate_by = 8

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        proveedores = Proveedores.objects.filter(nombre__icontains=query)
        return proveedores
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q', '')
        context['query'] = query
        return context

def proveedores(request, pk):
    prov = Proveedores.objects.get(id=pk)
    #un nombre con el que llamo a la variable : modelo objeto que voy a mandar
    context = {'prov': prov}
    #template, el render manda el contexto al template||
    return render(request, 'proveedores.html', context)



@permission_required('app.change_proveedores', login_url='/login/')
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






#pk es la referencia al id del articulo
def compras(request, pk):
    com = Compras.objects.get(id=pk)
    arts = CompraProd.objects.filter(idCompra_id=pk)
    #un nombre con el que llamo a la variable : modelo objeto que voy a mandar
    context = {'com': com, 'arts':arts}
    #template, el render manda el contexto al template||
    return render(request, 'compras.html', context)

class TablaCompras(ListView):
    model = Compras
    template_name = 'tablaCompras.html'
    context_object_name = 'Compras'
    paginate_by = 8

    # def get(self, request):
    #     query = request.GET.get('q', datetime.today())
    #     if not query:
    #         query = datetime.today()
    #     compras = Compras.objects.filter(fecha=query)
    #     context = {
    #         'Compras': compras,
    #         'query': query,
    #     }
    #     return render(request, self.template_name, context)

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        if not query:
            compras = Compras.objects.all()
        else:
            compras = Compras.objects.filter(fecha=query)
        return compras
    
    #para que se quede lo que busquemos 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q', '')
        context['query'] = query
        return context

    

class ComprasNuevo(CreateView):
    model = Compras
    form_class = ComprasForm
    template_name = 'ComprasForm.html'
    success_url = reverse_lazy('Compras')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = ComprasForm.CustomComprasFormset(self.request.POST)
        else:
            context['formset'] = ComprasForm.CustomComprasFormset()
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


class ComprasModif(UpdateView):
    model = Compras
    form_class = ComprasForm
    template_name = 'ComprasForm.html'
    success_url = reverse_lazy('Compras')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        compras = self.object
        total = compras.compraprod_set.aggregate(Sum('totalCompra'))['totalCompra__sum'] or 0
        context['total'] = total

        

        if self.request.POST:
            context['formset'] = ComprasForm.CustomComprasFormset(self.request.POST, instance=self.object)
        else:
            context['formset'] = ComprasForm.CustomComprasFormset(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid() and form.is_valid():
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))
        
class ComprasBorrar(DeleteView):
    model = Compras
    template_name = 'ComprasConfBorrar.html'
    success_url = reverse_lazy('Compras')


#pk es la referencia al id del articulo
def ventas(request, pk):
    ven = Ventas.objects.get(id=pk)
    ventaProd = VentaProd.objects.filter(idVenta_id=pk)

    #un nombre con el que llamo a la variable : modelo objeto que voy a mandar
    context = {'ven': ven, 'ventProd':VentaProd}
    #template, el render manda el contexto al template||
    return render(request, 'ventas.html', context)


class TablaVentas(ListView):
    model = Ventas
    template_name = 'tablaVentas.html'
    context_object_name = 'Ventas'
    paginate_by = 8

    # def get(self, request):
    #     query = request.GET.get('q', datetime.today())
    #     if not query:
    #         query = datetime.today()
    #     ventas = Ventas.objects.filter(fecha=query)
    #     context = {
    #         'Ventas': ventas,
    #         'query': query,
    #     }
    #     return render(request, self.template_name, context)


    def get_queryset(self):
        query = self.request.GET.get('q', '')
        if not query:
            ventas = Ventas.objects.all()
        else:
            ventas = Ventas.objects.filter(fecha=query)
        return ventas
    
    #para que se quede lo que busquemos 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q', '')
        context['query'] = query
        return context


class VentasNuevo(CreateView):
    model = Ventas
    form_class = VentasForm
    template_name = 'VentasForm.html'
    success_url = reverse_lazy('Ventas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.POST:
            context['formset'] = VentasForm.CustomVentasFormset(self.request.POST)
        else:
            context['formset'] = VentasForm.CustomVentasFormset()

        # Obtener información sobre los artículos y pasarla al contexto
        articles = Articulos.objects.all()
        
        articles_dict = {article.id: article for article in articles}
        context['articles_dict'] = articles_dict

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
    success_url = reverse_lazy('Ventas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        ventas = self.object
        total = ventas.ventaprod_set.aggregate(Sum('totalVenta'))['totalVenta__sum'] or 0
        print(total)
        context['total'] = total

        if self.request.POST:
            context['formset'] = VentasForm.CustomVentasFormset(self.request.POST, instance=self.object)
        else:
            context['formset'] = VentasForm.CustomVentasFormset(instance=self.object)
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
    template_name = 'VentasConfBorrar.html'
    success_url = reverse_lazy('Ventas')



def Logout(request):
    logout(request)
    return redirect('/index')

import io
from django.http import FileResponse
from django.db.models import Sum
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from .models import Ventas, VentaProd
from reportlab.lib.pagesizes import letter

def VentasPDF(request, pk):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=A4)

    textobj = c.beginText()
    
    w, h = A4
    

    c.setFont("Times-Roman", 40)  
    c.drawString(50, h- 50, "FACTURA")
    c.drawImage('proyectoRieVictoria\static\img\RV2.png', 350, h-130, 220, 110)

    c.setFont("Times-Bold", 12)  
    c.drawString(50, h - 90, "Dirección") 
    c.drawString(50, h - 130, "Télefono")  
    c.drawString(250, h - 130, "Gmail") 
    

    c.setFont("Times-Roman", 12)  
    c.drawString(50, h - 110, "Belgrano 259,Villa Dolores") 
    c.drawString(50, h - 144, "3544-543815")  
    c.drawString(250, h - 145, "Rievictoria@gmail.com") 
    

    ventas_queryset = Ventas.objects.filter(id=pk)
    ventasProd = VentaProd.objects.filter(idVenta=pk)
    

    for ventas in ventas_queryset:
        c.setFont("Times-Roman", 12)

        fecha_formateada = ventas.fecha.strftime("%d/%m/%Y")
        c.drawString(50, h-200, f"Fecha de venta:{fecha_formateada}")
        c.drawString(50, h-220, f"Empleado: {ventas.idEmpleado}")
        c.drawString(250, h-220, f"Cliente: {ventas.idClientes}")
        c.setFont("Times-Roman", 20)  
        c.rect(250, h-90,35,35)
        c.drawString(260, h-75, f"{ventas.tipoFactura}")
    
    c.setFont("Helvetica-Bold", 12)  
    c.drawString(50, h - 270, "Cód")
    c.drawString(80, h - 270, "Descripción")
    c.drawString(370, h - 270, "Precio")
    c.drawString(430, h - 270, "Cantidad")
    c.drawString(490, h - 270, "Importe")
    c.line(50, h -280, 549, h -280)


    
    ventasProd_list = list(ventasProd) 
    y_posicion = h - 300

    for indice, ventaProd in enumerate(ventasProd_list[:19]):
        c.setFont("Helvetica", 13) 

        c.drawString(50, y_posicion ,f"{ventaProd.idArticulos}")
        c.drawString( 370, y_posicion,f"${ventaProd.precioVenta}")
        c.drawString( 450, y_posicion,f"{ventaProd.cantidad}")

        subtotal_producto = ventaProd.precioVenta * ventaProd.cantidad
        c.drawString(490, y_posicion, f"${subtotal_producto}")

        y_posicion -= 25
    
    c.line(50, h -760, 549, h -760)
    c.setFont("Helvetica-Bold", 15)
    total = ventasProd.aggregate(Sum('totalVenta'))['totalVenta__sum'] or 0
    c.drawString( 450, h-790,f"Total ${total}")

    c.drawText(textobj)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename=f'factura_venta_{pk}.pdf')









