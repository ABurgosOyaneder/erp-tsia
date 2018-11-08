from django import forms
from apps.mod_venta_cot.models import Cotizacion , Cargo , Venta , Medio_pago , Cargo_venta , Producto_cotizacion


class CotizacionForm(forms.ModelForm):
	class Meta:
		model = Cotizacion

		fields = [
				'id_cliente',
				'id_prod_cot',
				'id_medio',
				'fecha_vencimiento',
				'subtotal',
				'impuestos',
				'descuento',
				'estado'
		]

class CargoForm(forms.ModelForm):
	class Meta:
		model = Cargo

		fields = [
				'nombre',
				'valor'
		]

class VentaForm(forms.ModelForm):
	class Meta:
		model = Venta

		fields = [
				'id_cotizacion',
				'total',
				'estado',
				'id_cargos'
		]

class Medio_pagoForm(forms.ModelForm):
	class Meta:
		model = Medio_pago

		fields = [
				'nombre',
				'descuento'
		]