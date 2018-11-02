from django.urls import path
from . import views

from apps.mod_adquisiciones.views import AdquisicionesList, AdquisicionesCreate, IngresoList, ProveedorList, OrdenAdqList

urlpatterns = [
    path('index/', views.index, name="index_adquisiciones"),
    path('adquisiciones/', AdquisicionesList.as_view(), name="adquisiciones_adquisiciones"),
    path('adquisiciones/create', AdquisicionesCreate.as_view(), name="adquisiciones_adquisiciones_create"),
    path('ingreso/', IngresoList.as_view(), name="adquisiciones_ingreso"),
    path('proveedor/', ProveedorList.as_view(), name="adquisiciones_proveedor"),
    path('orden_adquisicion/', OrdenAdqList.as_view(), name="adquisiciones_orden_adquisiciones"),
]

