from django import forms
from .models import *

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = [
            'nombre',
            'descripcion',
        ]

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'nombre',
            'cod_barra',
            'precio_compra',
            'precio_venta',
            'stock',
            'descripcion',
            'id_cat',
        ]
