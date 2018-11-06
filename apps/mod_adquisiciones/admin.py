from django.contrib import admin

# Register your models here.
from apps.mod_adquisiciones.models import Adquisicion , AdquisicionesProductos , Proveedor , Orden_adq

admin.site.register(Adquisicion)
admin.site.register(AdquisicionesProductos)
admin.site.register(Proveedor)
admin.site.register(Orden_adq)