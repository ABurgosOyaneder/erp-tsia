from django.urls import path

from . import views

app_name = 'facturacion'

urlpatterns = [
  path('', views.ListaDeFacturas.as_view(), name='lista_facturas'),
  path('new', views.CrearFactura.as_view(), name='nueva_factura'),
  path('edit/<int:pk>', views.ActualizarFactura.as_view(), name='editar_factura'),
  path('delete/<int:pk>', views.BorrarFactura.as_view(), name='borrar_factura'),

]