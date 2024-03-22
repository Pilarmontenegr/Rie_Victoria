from django import forms
from .models import Proveedores, Empleados , Clientes, Articulos, Ventas , VentaProd , CompraProd, Compras
from decimal import Decimal
from django.contrib import messages

from django.core.exceptions import ValidationError
from django.forms import ModelForm, Field, ValidationError, BooleanField, CharField

from django.shortcuts import get_object_or_404


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
    
    ventasFormset = forms.inlineformset_factory(Ventas, VentaProd, form=ventaProdForm, extra=1, max_num=20,can_delete=True, can_delete_extra=True)
    


##ultimo anda bien
    # from django.forms import formset_factory

    # class CustomVentasFormset(ventasFormset):
    #     def __init__(self, *args, **kwargs):
    #         super().__init__(*args, **kwargs)
    #         self.articulos_vendidos = set()

    #     def clean(self):
    #         super().clean()
    #         for form in self.forms:
    #             if form.cleaned_data.get('idArticulos') is not None and form.instance.pk is None:
    #                 cantidad = form.cleaned_data.get('cantidad')
    #                 if cantidad is not None:
    #                     precioVenta = form.instance.idArticulos.venta
    #                     totalVenta = precioVenta * cantidad
    #                     form.instance.precioVenta = precioVenta
    #                     form.instance.totalVenta = totalVenta

    #                     id_articulo = form.cleaned_data.get('idArticulos').id
    #                     articulo = Articulos.objects.get(id=id_articulo)

    #                     # Restar del stock la cantidad vendida
    #                     articulo.cantidad -= cantidad
    #                     articulo.save()
    #                     self.articulos_vendidos.add((id_articulo, cantidad))

    #             elif form.instance.pk and form.cleaned_data.get('cantidad') is not None:
    #                 cantidad = form.cleaned_data.get('cantidad')
    #                 initial_cantidad = form.initial['cantidad']

    #                 if cantidad != initial_cantidad:  # ver si se modifico la cantidad
    #                     id_articulo = form.cleaned_data.get('idArticulos').id
    #                     articulo = Articulos.objects.get(id=id_articulo)
    #                     diferencia = initial_cantidad - cantidad

    #                     # Ajustar el stock con la diferencia
    #                     articulo.cantidad += diferencia
    #                     articulo.save()
    #                     self.articulos_vendidos.discard((id_articulo, initial_cantidad))  # Eliminar la venta anterior del conjunto

        
#ultimo anduco bien 1/3:
    # from django import forms

    # class CustomVentasFormset(ventasFormset):
    #     def __init__(self, *args, **kwargs):
    #         super().__init__(*args, **kwargs)
    #         self.articulos_vendidos = set()

    #     def clean(self):
    #         cleaned_data = super().clean()
    #         for form in self.forms:
    #             cantidad = form.cleaned_data.get('cantidad')
    #             id_articulo = form.cleaned_data.get('idArticulos').id if form.cleaned_data.get('idArticulos') else None


    #             if form.cleaned_data.get('DELETE') and cantidad is not None and id_articulo is not None:
    #                 articulo = Articulos.objects.get(id=id_articulo)
    #                 articulo.cantidad += cantidad
    #                 articulo.save()
    #                 self.articulos_vendidos.discard((id_articulo, cantidad))  # Eliminar la venta del conjunto

    #             if id_articulo and form.instance.pk is None:
    #                 cantidad = form.cleaned_data.get('cantidad')
    #                 if cantidad is not None:
    #                     precioVenta = form.instance.idArticulos.venta
    #                     totalVenta = precioVenta * cantidad
    #                     form.instance.precioVenta = precioVenta
    #                     form.instance.totalVenta = totalVenta

    #                     articulo = Articulos.objects.get(id=id_articulo)

    #                     # Restar del stock la cantidad vendida
    #                     articulo.cantidad -= cantidad
    #                     articulo.save()
    #                     self.articulos_vendidos.add((id_articulo, cantidad))

    #             elif form.instance.pk and cantidad is not None:
    #                 initial_cantidad = form.initial.get('cantidad')
    #                 if initial_cantidad is not None and cantidad != initial_cantidad:  # ver si se modifico la cantidad
    #                     diferencia = initial_cantidad - cantidad

    #                     articulo = Articulos.objects.get(id=id_articulo)

    #                     # Ajustar el stock con la diferencia
    #                     articulo.cantidad += diferencia
    #                     articulo.save()
    #                     self.articulos_vendidos.discard((id_articulo, initial_cantidad))  # Eliminar la venta anterior del conjunto

    #         return cleaned_data


    # from django import forms

    # class CustomVentasFormset(ventasFormset):
    #     def __init__(self, *args, **kwargs):
    #         super().__init__(*args, **kwargs)
    #         self.articulos_vendidos = set()

    #     def clean(self):
    #         cleaned_data = super().clean()
            
    #         for form in self.forms:
    #             cantidad = form.cleaned_data.get('cantidad')
    #             id_articulo = form.cleaned_data.get('idArticulos').id if form.cleaned_data.get('idArticulos') else None


    #             if form.cleaned_data.get('DELETE') and cantidad is not None and id_articulo is not None:
    #                 articulo = Articulos.objects.get(id=id_articulo)
    #                 articulo.cantidad += cantidad
    #                 articulo.save()
    #                 self.articulos_vendidos.discard((id_articulo, cantidad))  # Eliminar la venta del conjunto

    #             if id_articulo and form.instance.pk is None:
    #                 cantidad = form.cleaned_data.get('cantidad')
    #                 if cantidad is not None:
    #                     precioVenta = form.instance.idArticulos.venta
    #                     totalVenta = precioVenta * cantidad
    #                     form.instance.precioVenta = precioVenta
    #                     form.instance.totalVenta = totalVenta

    #                     articulo = Articulos.objects.get(id=id_articulo)

    #                     # Restar del stock la cantidad vendida
    #                     articulo.cantidad -= cantidad
    #                     articulo.save()
    #                     self.articulos_vendidos.add((id_articulo, cantidad))

    #             elif form.instance.pk and cantidad is not None:
    #                 initial_cantidad = form.initial.get('cantidad')
    #                 if initial_cantidad is not None and cantidad != initial_cantidad:  # ver si se modifico la cantidad
    #                     diferencia = initial_cantidad - cantidad

    #                     articulo = Articulos.objects.get(id=id_articulo)

    #                     # Ajustar el stock con la diferencia
    #                     articulo.cantidad += diferencia
    #                     articulo.save()
    #                     self.articulos_vendidos.discard((id_articulo, initial_cantidad))  # Eliminar la venta anterior del conjunto

    #         return cleaned_data

############ultimooo 17/3
    from django import forms
    from django.core.exceptions import ValidationError
    from .models import Articulos

    class CustomVentasFormset(ventasFormset):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.articulos_vendidos = set()
            self.no_stock = []

        def clean(self):
            cleaned_data = super().clean()
            
            for form in self.forms:
                cantidad = form.cleaned_data.get('cantidad')
                id_articulo = form.cleaned_data.get('idArticulos').id if form.cleaned_data.get('idArticulos') else None

                if form.cleaned_data.get('DELETE') and cantidad is not None and id_articulo is not None:
                    articulo = Articulos.objects.get(id=id_articulo)
                    articulo.cantidad += cantidad
                    articulo.save()
                    self.articulos_vendidos.discard((id_articulo, cantidad))  # Eliminar la venta 

                if id_articulo and form.instance.pk is None:
                    cantidad = form.cleaned_data.get('cantidad')
                    if cantidad is not None:
                        precioVenta = form.instance.idArticulos.venta
                        totalVenta = precioVenta * cantidad
                        form.instance.precioVenta = precioVenta
                        form.instance.totalVenta = totalVenta

                        articulo = Articulos.objects.get(id=id_articulo)


                        #ACA SI LA CANTIDAD ES MAYOR AL STOCK
                        if cantidad > articulo.cantidad:
                            print(cantidad)
                            print(articulo.cantidad)
                            self.no_stock.append(articulo)
                            print(self.no_stock)
                           
                        if self.no_stock:
                            raise ValidationError("No hay stock")
                        
                        else:  
                            articulo.cantidad -= cantidad
                            articulo.save()
                            self.articulos_vendidos.add((id_articulo, cantidad))

                                
                        

                elif form.instance.pk and cantidad is not None:
                    initial_cantidad = form.initial.get('cantidad')
                    if initial_cantidad is not None and cantidad != initial_cantidad:  # ver si se modifico la cantidad
                        diferencia = initial_cantidad - cantidad

                        articulo = Articulos.objects.get(id=id_articulo)

                        
                        articulo.cantidad += diferencia
                        articulo.save()
                        self.articulos_vendidos.discard((id_articulo, initial_cantidad))  # Eliminar la venta anterior del conjunto

            return cleaned_data



    # from django import forms
    # from django.core.exceptions import ValidationError
    # from .models import Articulos

    # class CustomVentasFormset(ventasFormset):
    #     def __init__(self, *args, **kwargs):
    #         super().__init__(*args, **kwargs)
    #         self.articulos_vendidos = set()
        
    #     def clean(self):
    #         cleaned_data = super().clean()
            
    #         for form in self.forms:
    #             cantidad = form.cleaned_data.get('cantidad')
    #             id_articulo = form.cleaned_data.get('idArticulos').id if form.cleaned_data.get('idArticulos') else None

    #             if form.cleaned_data.get('DELETE') and cantidad is not None and id_articulo is not None:
    #                 articulo = Articulos.objects.get(id=id_articulo)
    #                 articulo.cantidad += cantidad
    #                 articulo.save()
    #                 self.articulos_vendidos.discard((id_articulo, cantidad))  # Eliminar la venta 

    #             if id_articulo and form.instance.pk is None:
    #                 cantidad = form.cleaned_data.get('cantidad')
    #                 if cantidad is not None:
    #                     precioVenta = form.instance.idArticulos.venta
    #                     totalVenta = precioVenta * cantidad
    #                     form.instance.precioVenta = precioVenta
    #                     form.instance.totalVenta = totalVenta

    #                     articulo = Articulos.objects.get(id=id_articulo)

                        
                                
    #             elif form.instance.pk and cantidad is not None:
    #                 initial_cantidad = form.initial.get('cantidad')
    #                 if initial_cantidad is not None and cantidad != initial_cantidad:  # ver si se modifico la cantidad
    #                     diferencia = initial_cantidad - cantidad

    #                     articulo = Articulos.objects.get(id=id_articulo)

                        
    #                     articulo.cantidad += diferencia
    #                     articulo.save()
    #                     self.articulos_vendidos.discard((id_articulo, initial_cantidad))  # Eliminar la venta anterior del conjunto
            
    #         return cleaned_data
        



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
    
    comprasFormset = forms.inlineformset_factory(Compras, CompraProd, form=CompraProdForm, extra=10)

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

      
   
                   