from django.shortcuts import render, redirect
from apps.mod_venta_cot.models import Cotizacion , Cargo , Venta , Medio_pago , Cargo_venta , Producto_cotizacion
from apps.mod_venta_cot.forms import CotizacionForm , CargoForm , VentaForm , Medio_pagoForm
from django.views.generic import CreateView , UpdateView , ListView , DeleteView
from django.urls import reverse_lazy

# Create your views here.

def index(request):
    return render(request,'mod_venta_cot/index.html')

def cotizacion(request):
    return render(request,'mod_venta_cot/cotizacion.html')

def venta(request):
    return render(request,'mod_venta_cot/venta.html')       

class CreateCotizacion(CreateView):
	model = Cotizacion
	form_class = CotizacionForm    
	template_name = 'mod_venta_cot/crear_cotizacion.html' 
	success_url = reverse_lazy('index')

class ListCotizacion(ListView):
	model =	Cotizacion
	template_name = 'mod_venta_cot/listar_cotizacion.html'

class UpdateCotizacion(UpdateView):
	model = Cotizacion
	form_class = CotizacionForm    
	template_name = 'mod_venta_cot/crear_cotizacion.html' 
	success_url = reverse_lazy('index')	

class DeleteCotizacion(DeleteView):
	model = Cotizacion
	template_name = 'mod_venta_cot/eliminar_cotizacion.html' 
	success_url = reverse_lazy('index')		
"""
def crearcotizacion(request):
	if request.method == 'POST':
		form = CotizacionForm(request.POST)
		if form.is_valid():
			form.save()
			message.add_message(request, message.SUCCESS,"La cotización ha sido creada!")
			return redirect('index_venta_cot')
	else:
		form = CotizacionForm()
	return render(request,'mod_venta_cot/crear_cotizacion.html', {'form':form})	    

def listarcotizacion(request):
	cotizacion = Cotizacion.objects.all()
	contexto = {'cotizacion':cotizacion}
	return render(request,'mod_venta_cot/listar_cotizacion.html', contexto)	

def editarcotizacion(request,id):
	cotizacion = Cotizacion.objects.get(id = id)
	if request.method == 'GET':
		form = CotizacionForm(instance = cotizacion)
	else:
		form = CotizacionForm(request.POST, instance = cotizacion)
		if form.is_valid():
			form.save()
		return redirect('index_venta_cot')
	return render(request, 'mod_venta_cot/crear_cotizacion.html', {'form':form})	

def eliminarcotizacion(request,id):
	cotizacion = Cotizacion.objects.get(id = id)
	if request.method == 'POST':
		cotizacion.delete()
		return redirect('index_venta_cot')
	return render(request, 'mod_venta_cot/eliminar_cotizacion.html', {'cotizacion':cotizacion})				
"""
