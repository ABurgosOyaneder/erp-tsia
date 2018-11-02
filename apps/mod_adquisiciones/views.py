from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView , DeleteView
from django.urls import reverse_lazy

from apps.mod_adquisiciones.models import Adquisicion , Ingreso , Proveedor , Orden_adq
from apps.mod_adquisiciones.form import AdquisicionForm

def index(request):
    return render(request,'mod_adquisiciones/index.html')

def adquisiciones(request):
    return render(request,'mod_adquisiciones/adquisiciones.html')

class AdquisicionesList(ListView):
	model = Adquisicion
	template_name = 'mod_adquisiciones/adquisiciones_list.html'

class AdquisicionesCreate(CreateView):
	model = Adquisicion
	form_class = AdquisicionForm
	template_name = 'mod_adquisiciones/adquisiciones_form.html'
	success_url = reverse_lazy('adquisiciones_adquisiciones')

class AdquisicionesUpdate(UpdateView):
	model = Adquisicion
	form_class = AdquisicionForm
	template_name = 'mod_adquisiciones/adquisiciones_form.html'
	success_url = reverse_lazy('adquisiciones_adquisiciones')

class AdquisicionesDelete(DeleteView):
	model = Adquisicion
	form_class = AdquisicionForm
	template_name = 'mod_adquisiciones/adquisiciones_delete.html'
	success_url = reverse_lazy('adquisiciones_adquisiciones')




class IngresoList(ListView):
	model = Ingreso
	template_name = 'mod_adquisiciones/ingreso_list.html'

class ProveedorList(ListView):
	model = Proveedor
	template_name = 'mod_adquisiciones/proveedor_list.html'

class OrdenAdqList(ListView):
	model = Orden_adq
	template_name = 'mod_adquisiciones/orden_adq_list.html'

