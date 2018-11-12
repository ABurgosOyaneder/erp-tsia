from django.urls import path
from . import views

from apps.mod_contabilidad.views import ContabilidadList, ContabilidadCreate, ContabilidadUpdate, ContabilidadDelete
from apps.mod_contabilidad.views import ActivoFijoList, ActivoFijoCreate, ActivoFijoUpdate, ActivoFijoDelete

urlpatterns = [
    path('index/', views.index, name="index_contabilidad"),

    path('activo/', ActivoFijoList.as_view(), name="contabilidad_activos_fijos"),
    path('activo/create', ActivoFijoCreate.as_view(), name="contabilidad_activos_fijos_create"),
    path('activo/update/<int:pk>/', ActivoFijoUpdate.as_view(), name="contabilidad_activos_fijos_update"),
    path('activo/delete/<int:pk>/', ActivoFijoDelete.as_view(), name="contabilidad_activos_fijos_delete"),
]