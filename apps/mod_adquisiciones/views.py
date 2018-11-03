from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView , DeleteView
from django.urls import reverse_lazy

from apps.mod_adquisiciones.models import Adquisicion , Ingreso , Proveedor , Orden_adq
from apps.mod_adquisiciones.form import AdquisicionForm, IngresoForm, ProveedorForm, OrdenAdqForm

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

class IngresoCreate(CreateView):
	model = Ingreso
	form_class = IngresoForm
	template_name = 'mod_adquisiciones/ingreso_form.html'
	success_url = reverse_lazy('adquisiciones_adquisiciones')

class IngresoUpdate(UpdateView):
	model = Ingreso
	form_class = IngresoForm
	template_name = 'mod_adquisiciones/ingreso_form.html'
	success_url = reverse_lazy('adquisiciones_adquisiciones')

class IngresoDelete(DeleteView):
	model = Ingreso
	form_class = IngresoForm
	template_name = 'mod_adquisiciones/ingreso_delete.html'
	success_url = reverse_lazy('adquisiciones_adquisiciones')



class ProveedorList(ListView):
	model = Proveedor
	template_name = 'mod_adquisiciones/proveedor_list.html'

class ProveedorCreate(CreateView):
	model = Proveedor
	form_class = ProveedorForm
	template_name = 'mod_adquisiciones/proveedor_form.html'
	success_url = reverse_lazy('adquisiciones_adquisiciones')

class ProveedorUpdate(UpdateView):
	model = Proveedor
	form_class = ProveedorForm
	template_name = 'mod_adquisiciones/proveedor_form.html'
	success_url = reverse_lazy('adquisiciones_adquisiciones')

class ProveedorDelete(DeleteView):
	model = Proveedor
	form_class = ProveedorForm
	template_name = 'mod_adquisiciones/proveedor_delete.html'
	success_url = reverse_lazy('adquisiciones_adquisiciones')



class OrdenAdqList(ListView):
	model = Orden_adq
	template_name = 'mod_adquisiciones/ord_adq_list.html'

class OrdenAdqCreate(CreateView):
	model = Orden_adq
	form_class = OrdenAdqForm
	template_name = 'mod_adquisiciones/ord_adq_form.html'
	success_url = reverse_lazy('adquisiciones_adquisiciones')

class OrdenAdqUpdate(UpdateView):
	model = Orden_adq
	form_class = OrdenAdqForm
	template_name = 'mod_adquisiciones/ord_adq_form.html'
	success_url = reverse_lazy('adquisiciones_adquisiciones')

class OrdenAdqDelete(DeleteView):
	model = Orden_adq
	form_class = OrdenAdqForm
	template_name = 'mod_adquisiciones/ord_adq_delete.html'
	success_url = reverse_lazy('adquisiciones_adquisiciones')

