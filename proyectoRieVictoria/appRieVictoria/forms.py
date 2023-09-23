from django import forms
from .models import Proveedores, Empleados , Clientes, Articulos, Ventas , ventaProd

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
        fields = ('descripcion', 'costo', 'venta', 'cantidad', 'talle', 'tipoPrenda'  )
        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'costo': forms.NumberInput(attrs={'class': 'form-control'}),
            'venta': forms.NumberInput(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'talle': forms.TextInput(attrs={'class': 'form-control'}),
            'tipoPrenda': forms.TextInput(attrs={'class': 'form-control'}),
        }




class ventaProdForm(forms.ModelForm):
    class Meta:
        model = ventaProd
        fields = '__all__'
        widgets = {
            'idVenta': forms.Select(attrs={'class': 'form-select'}),
            'idArticulos': forms.Select(attrs={'class': 'form-select'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class VentasForm(forms.ModelForm):
    class Meta:
        model = Ventas
        fields= '__all__'
        widgets= {
            'idEmpleado': forms.Select(attrs={'class': 'form-select'}),
            'idClientes': forms.Select(attrs={'class': 'form-select'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'articulos': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'tipoFactura': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
ventasFormset = forms.inlineformset_factory(Ventas, ventaProd, form=ventaProdForm, extra=1)

