from django import forms
from .models import Proveedores, Empleados , Clientes, Articulos, Ventas , VentaProd , CompraProd, Compras
from decimal import Decimal
class ProveedoresForm(forms.ModelForm):
    class Meta:
        model = Proveedores
        fields = ('nombre', 'direccion', 'Email', 'cuit', 'telefono'  )
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'Email': forms.TextInput(attrs={'class': 'form-control'}),
            'cuit': forms.NumberInput(attrs={'class': 'form-control'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class EmpleadosForm(forms.ModelForm):
    class Meta:
        model = Empleados
        fields = ('nombre', 'direccion', 'Email', 'telefono'  )
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'Email': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ClientesForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ('nombre', 'direccion', 'DNI', 'telefono'  )
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'DNI': forms.NumberInput(attrs={'class': 'form-control'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ArticulosForm(forms.ModelForm):
    class Meta:
        model = Articulos
        fields = ('descripcion', 'venta', 'cantidad', 'talle', 'tipoPrenda'  )
        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            #'costo': forms.NumberInput(attrs={'class': 'form-control'}),
            'venta': forms.NumberInput(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'talle': forms.TextInput(attrs={'class': 'form-control'}),
            'tipoPrenda': forms.Select(attrs={'class': 'form form-select'}),
            
        }

class ventaProdForm(forms.ModelForm):
    class Meta:
        model = VentaProd
        fields = '__all__'
        widgets = {
            'idVenta': forms.Select(attrs={'class': 'form-select'}),
            'idArticulos': forms.Select(attrs={'class': 'form-select'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'precioVenta': forms.NumberInput(attrs={'class': 'form-control'}),
            'totalVenta': forms.NumberInput(attrs={'class': 'form-control'}),  
        }
    
    
class VentasForm(forms.ModelForm):
    class Meta:
        model = Ventas
        fields= '__all__'
        exclude = ['articulos']
        widgets= {
            'idEmpleado': forms.Select(attrs={'class': 'form-select'}),
            'idClientes': forms.Select(attrs={'class': 'form-select'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'tipoFactura': forms.Select(attrs={'class': 'form-select'}),
        }
    
    ventasFormset = forms.inlineformset_factory(Ventas, VentaProd, form=ventaProdForm, extra=1, max_num=20)

    # class CustomVentasFormset(ventasFormset):
    #     def clean(self):
    #         super().clean()
    #         for form in self.forms:
    #             cantidad = form.cleaned_data.get('cantidad')
    #             if cantidad is not None:
    #                 precioVenta = form.instance.idArticulos.venta
    #                 totalVenta =  precioVenta * cantidad
    #                 form.instance.precioVenta = precioVenta
    #                 form.instance.totalVenta = totalVenta
    
 

    class CustomVentasFormset(ventasFormset):

        def clean(self):
            super().clean()
            for form in self.forms:
                cantidad = form.cleaned_data.get('cantidad')
                if cantidad is not None:
                    precioVenta = form.instance.idArticulos.venta
                    totalVenta =  precioVenta * cantidad
                    form.instance.precioVenta = precioVenta
                    form.instance.totalVenta = totalVenta

                    id_articulo = form.cleaned_data.get('idArticulos').id
                    articulo = Articulos.objects.get(id=id_articulo)

                    articulo.cantidad -= cantidad
                    articulo.save()


    # class CustomVentasFormset(forms.BaseInlineFormSet):
    #     def clean(self):
    #     super().clean()
    #     total_venta_por_articulo = {}

    #     # Calcular la cantidad total vendida por cada artículo
    #     for form in self.forms:
    #         cantidad = form.cleaned_data.get('cantidad')
    #         id_articulo = form.cleaned_data.get('idArticulos').id

    #         if cantidad is not None:
    #             if id_articulo in total_venta_por_articulo:
    #                 total_venta_por_articulo[id_articulo] += cantidad
    #             else:
    #                 total_venta_por_articulo[id_articulo] = cantidad

    #     # Actualizar el stock de cada artículo
    #     for id_articulo, cantidad_vendida in total_venta_por_articulo.items():
    #         articulo = Articulos.objects.get(id=id_articulo)
    #         articulo.cantidad -= cantidad_vendida
    #         articulo.save()









                    


class CompraProdForm(forms.ModelForm):
    class Meta:
        model = CompraProd
        fields = '__all__'
        widgets = {
            'idCompra': forms.Select(attrs={'class': 'form-select'}),
            'idArticulos': forms.Select(attrs={'class': 'form-select'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'totalCompra': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ComprasForm(forms.ModelForm):
    class Meta:
        model = Compras
        fields= '__all__'
        exclude = ['articulos']
        widgets= {
            'idProveedor': forms.Select(attrs={'class': 'form-select'}),
            'idEmpleado': forms.Select(attrs={'class': 'form-select'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            
        }
    
    comprasFormset = forms.inlineformset_factory(Compras, CompraProd, form=CompraProdForm, extra=1)

    class CustomComprasFormset(comprasFormset):
        def clean(self):
            super().clean()
            for form in self.forms:
                cantidad = form.cleaned_data.get('cantidad')
                if cantidad is not None:
                    precio = form.instance.precio
                    totalCompra =  precio * cantidad
                    form.instance.precio  = precio
                    form.instance.totalCompra = totalCompra

      
   
                   