from django.shortcuts import render
from .forms import *
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

def index(request):
    return render(request,'mod_inventario/index.html')

# Clase Categoria

class CrearCategoria(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'mod_inventario/crear_categoria.html'
    success_url = reverse_lazy('listar_categoria')

class ListarCategoria(ListView):
    model = Categoria
    template_name = 'mod_inventario/listar_categoria.html'

class EditarCategoria(UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'mod_inventario/crear_categoria.html'
    success_url = reverse_lazy('listar_categoria')

class EliminarCategoria(DeleteView):
    model = Categoria
    template_name = 'mod_inventario/eliminar_categoria.html'
    success_url = reverse_lazy('listar_categoria')

# Clase Producto

class CrearProducto(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'mod_inventario/crear_producto.html'
    success_url = reverse_lazy('index_inventario')

class ListarProducto(ListView):
    model = Producto
    template_name = 'mod_inventario/listar_producto.html'

class EditarProducto(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'mod_inventario/crear_producto.html'
    success_url = reverse_lazy('index_inventario')

class EliminarProducto(DeleteView):
    model = Producto
    template_name = 'mod_inventario/eliminar_producto.html'
    success_url = reverse_lazy('index_inventario')