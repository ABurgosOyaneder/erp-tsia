from django.urls import path
from . import views

from apps.mod_contabilidad.views import ActivoFijoList, ActivoFijoCreate, ActivoUpdate, ActivoDelete

urlpatterns = [
    path('contabilidad/', views.index, name="index_contabilidad"),

    path('activo/', ActivoFijoList.as_view(), name="contabilidad_activos_fijos"),
    path('activo/create', ActivoFijoCreate.as_view(), name="contabilidad_activos_fijos_create"),
    path('activo/update/<int:pk>/', ActivoFijoUpdate.as_view(), name="contabilidad_activos_fijos_update"),
    path('activo/delete/<int:pk>/', ActivoFijoDelete.as_view(), name="contabilidad_activos_fijos_delete"),
]