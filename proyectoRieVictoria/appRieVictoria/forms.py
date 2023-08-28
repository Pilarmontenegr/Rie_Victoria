from django import forms
from .models import Proveedores

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