from django.urls import path
from . import views


#Aqui van la urls de su modulo
urlpatterns = [
    path('venta_cot/', views.index, name="index_venta_cot"),
    path('cotizacion/', views.cotizacion, name="cotizacion_venta_cot"),
    path('venta/', views.venta, name="venta_venta_cot")
]