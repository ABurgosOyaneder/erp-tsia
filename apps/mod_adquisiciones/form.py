from django import forms

from apps.mod_adquisiciones.models import Adquisicion, Ingreso , Proveedor , Orden_adq

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

class IngresoForm(forms.ModelForm):
	class Meta:
		model = Ingreso

		fields = {
			'cantidad',
			'precio_compra',
			'id_adq',
			'id_prod'
		}

		labels = {
			'cantidad' : 'Cantidad',
			'precio_compra' : 'Precio de Compra',
			'id_adq' : 'Adquisicion',
			'id_prod' : 'Producto'
		}

		widgets = {
			'cantidad' : forms.NumberInput(attrs={'class':'form-control'}),
			'precio_compra' : forms.NumberInput(attrs={'class':'form-control'}),
			'id_adq' : forms.Select(attrs={'class':'form-control'}),
			'id_prod' : forms.Select(attrs={'class':'form-control'}),
		}

class ProveedorForm(forms.ModelForm):
	class Meta:
		model = Proveedor

		fields = {
			'rut',
			'nombre',
			'direccion',
			'telefono',
			'nom_cont',
			'giro',
		}

		labels = {
			'rut' : 'Rut',
			'nombre' : 'Nombre',
			'direccion' : 'Direccon',
			'telefono' : 'Telefono',
			'nom_cont' : 'Nombre Conasdassad',
			'giro' : 'Giro',
		}

		widgets = {
			'id_cat' : forms.Select(attrs={'class':'form-control'}),
			'cantidad' : forms.NumberInput(attrs={'class':'form-control'}),
			'precio_compra' : forms.NumberInput(attrs={'class':'form-control'}),

			'rut' : forms.TextInput(attrs={'class':'form-control'}),
			'nombre' : forms.TextInput(attrs={'class':'form-control'}),
			'direccion' : forms.TextInput(attrs={'class':'form-control'}),
			'telefono' : forms.TextInput(attrs={'class':'form-control'}),
			'nom_cont' : forms.TextInput(attrs={'class':'form-control'}),
			'giro' : forms.TextInput(attrs={'class':'form-control'}),
		}

class OrdenAdqForm(forms.ModelForm):
	class Meta:
		model = Orden_adq

		fields = {
			'id_adq',
			'id_prov',
			'precio_compra',
		}

		labels = {
			'id_adq' : 'Adquisicion',
			'id_prov' : 'Proveedor',
			'precio_compra' : 'Precio de Compra',
		}

		widgets = {
			'id_adq' : forms.Select(attrs={'class':'form-control'}),
			'id_prov' : forms.Select(attrs={'class':'form-control'}),
			'precio_compra' : forms.NumberInput(attrs={'class':'form-control'}),
		}