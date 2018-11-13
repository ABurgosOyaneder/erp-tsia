from django.urls import path
from . import views

urlpatterns = [
    path('inventario/', views.index, name="index_inventario"),
    # Clase Categoria
    path('inventario/crear_categoria/', views.CrearCategoria.as_view(), name="crear_categoria"),
    path('inventario/listar_categoria/', views.ListarCategoria.as_view(), name="listar_categoria"),
    path('inventario/editar_categoria/<int:pk>/', views.EditarCategoria.as_view(), name="editar_categoria"),
    path('inventario/eliminar_categoria/<int:pk>/', views.EliminarCategoria.as_view(), name="eliminar_categoria"),
    # Clase Producto
    path('inventario/crear_producto/', views.CrearProducto.as_view(), name="crear_producto"),
    path('inventario/listar_producto/', views.ListarProducto.as_view(), name="listar_producto"),
    #path('inventario/editar_producto/<int:pk>/', views.EditarProducto.as_view(), name="editar_producto"),
    #path('inventario/eliminar_producto/<int:pk>/', views.EliminarProducto.as_view(), name="eliminar_producto"),
]