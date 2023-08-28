from django import forms
from .models import Articulos

class ArticulosForm(forms.ModelForm):
    class Meta:
        model = Articulos
        fields = ('descripcion', 'costo', 'venta', 'cantidad', 'talle', 'tipoPrenda')
        widgets = {
            'descripcion': forms.TextIput(attrs={'class': 'form-control'}),
            'costo': forms.NumberInput(attrs={'class': 'form-control'}),
            'venta': forms.NumberInput(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextIput(attrs={'class': 'form-control'}),
        }