from django.urls import path
from . import views

from apps.mod_adquisiciones.views import AdquisicionesList, AdquisicionesCreate, AdquisicionesUpdate, AdquisicionesDelete, IngresoList, ProveedorList, OrdenAdqList

urlpatterns = [
    path('index/', views.index, name="index_adquisiciones"),
    path('adquisiciones/', AdquisicionesList.as_view(), name="adquisiciones_adquisiciones"),
    path('adquisiciones/create', AdquisicionesCreate.as_view(), name="adquisiciones_adquisiciones_create"),
    path('adquisiciones/update/<int:pk>/', AdquisicionesUpdate.as_view(), name="adquisiciones_adquisiciones_update"),
    path('adquisiciones/delete/<int:pk>/', AdquisicionesDelete.as_view(), name="adquisiciones_adquisiciones_delete"),

    path('ingreso/', IngresoList.as_view(), name="adquisiciones_ingresos"),
    path('proveedor/', ProveedorList.as_view(), name="adquisiciones_proveedores"),
    path('orden_adquisicion/', OrdenAdqList.as_view(), name="adquisiciones_ordenes_adquisiciones"),
]

