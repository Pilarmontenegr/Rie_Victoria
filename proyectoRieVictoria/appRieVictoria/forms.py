from django import forms
from .models import Proveedores, Empleados , Clientes

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