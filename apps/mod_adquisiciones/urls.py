from django.urls import path
from . import views

from apps.mod_adquisiciones.views import AdquisicionesList, AdquisicionesCreate, AdquisicionesUpdate, AdquisicionesDelete
from apps.mod_adquisiciones.views import IngresoList, IngresoCreate, IngresoUpdate, IngresoDelete
from apps.mod_adquisiciones.views import ProveedorList, ProveedorCreate, ProveedorUpdate, ProveedorDelete
from apps.mod_adquisiciones.views import OrdenAdqList, OrdenAdqCreate, OrdenAdqUpdate, OrdenAdqDelete

urlpatterns = [
    path('index/', views.index, name="index_adquisiciones"),

    path('adquisiciones/', AdquisicionesList.as_view(), name="adquisiciones_adquisiciones"),
    path('adquisiciones/create', AdquisicionesCreate.as_view(), name="adquisiciones_adquisiciones_create"),
    path('adquisiciones/update/<int:pk>/', AdquisicionesUpdate.as_view(), name="adquisiciones_adquisiciones_update"),
    path('adquisiciones/delete/<int:pk>/', AdquisicionesDelete.as_view(), name="adquisiciones_adquisiciones_delete"),

    path('ingreso/', IngresoList.as_view(), name="adquisiciones_ingresos"),
    path('ingreso/create', IngresoCreate.as_view(), name="adquisiciones_ingresos_create"),
    path('ingreso/update/<int:pk>/', IngresoUpdate.as_view(), name="adquisiciones_ingresos_update"),
    path('ingreso/delete/<int:pk>/', IngresoDelete.as_view(), name="adquisiciones_ingresos_delete"),

    path('proveedor/', ProveedorList.as_view(), name="adquisiciones_proveedores"),
    path('proveedor/create', ProveedorCreate.as_view(), name="adquisiciones_proveedor_create"),
    path('proveedor/update/<int:pk>/', ProveedorUpdate.as_view(), name="adquisiciones_proveedor_update"),
    path('proveedor/delete/<int:pk>/', ProveedorDelete.as_view(), name="adquisiciones_proveedor_delete"),

    path('orden_adquisicion/', OrdenAdqList.as_view(), name="adquisiciones_ordenes_adquisiciones"),
    path('orden_adquisicion/create', OrdenAdqCreate.as_view(), name="adquisiciones_ordenes_create"),
    path('orden_adquisicion/update/<int:pk>/', OrdenAdqUpdate.as_view(), name="adquisiciones_ordenes_update"),
    path('orden_adquisicion/delete/<int:pk>/', OrdenAdqDelete.as_view(), name="adquisiciones_ordenes_delete"),
]

