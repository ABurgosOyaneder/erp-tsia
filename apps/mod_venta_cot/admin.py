from django.contrib import admin
from apps.mod_venta_cot.models import Cotizacion , Cargo , Venta , Medio_pago , Cargo_venta , Producto_cotizacion

# Register your models here.

admin.site.register(Cotizacion)
admin.site.register(Cargo)
admin.site.register(Venta)
admin.site.register(Medio_pago)
admin.site.register(Cargo_venta)
admin.site.register(Producto_cotizacion)