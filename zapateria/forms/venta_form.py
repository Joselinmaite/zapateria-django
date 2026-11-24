from django import forms
from zapateria.models import Venta


class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['cliente', 'fecha_venta', 'productos', 'observaciones']
        widgets = {
            'cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_venta': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'productos': forms.SelectMultiple(attrs={'class': 'form-control', 'size': 6}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
