from django.urls import path
from . import views


#Aqui van la urls de su modulo
urlpatterns = [
    path('venta_cot/', views.index, name="index_venta_cot"),
    #path('cotizacion/', views.cotizacion, name="cotizacion_venta_cot"),
    #path('venta/', views.venta, name="venta_venta_cot"),
    path('crear_cotizacion/', views.CreateCotizacion.as_view(), name="crearcotizacion_venta_cot"),
    path('listar_cotizacion/', views.ListCotizacion.as_view(), name="listarcotizacion_venta_cot"),
    path('editar_cotizacion/(?P<pk>\d+)/', views.UpdateCotizacion.as_view(), name="editarcotizacion_venta_cot"),
    path('eliminar_cotizacion/(?P<pk>\d+)/', views.DeleteCotizacion.as_view(), name="eliminarcotizacion_venta_cot")
]
