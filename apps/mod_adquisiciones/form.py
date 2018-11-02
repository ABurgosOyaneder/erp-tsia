from django import forms

from apps.mod_adquisiciones.models import Adquisicion

class AdquisicionForm(forms.ModelForm):
	class Meta:
		model = Adquisicion

		fields = {
			'id_cat',
			#'id_prod',
			'cantidad',
			'precio_compra',
		}

		labels = {
			'id_cat' : 'Categoria',
			#'id_prod' : 'Productos',
			'cantidad' : 'Cantidad',
			'precio_compra' : 'Precio de Compra',
		}

		widgets = {
			'id_cat' : forms.Select(attrs={'class':'form-control'}),
			#'id_prod' : forms.CheckboxSelectMultiple(attrs={'class':'form-control'}),
			'cantidad' : forms.NumberInput(attrs={'class':'form-control'}),
			'precio_compra' : forms.NumberInput(attrs={'class':'form-control'}),
		}