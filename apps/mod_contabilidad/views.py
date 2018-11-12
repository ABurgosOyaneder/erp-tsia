from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView , DeleteView
from django.urls import reverse_lazy

from apps.mod_contabilidad.models import Contabilidad, ActivoFijo
from apps.mod_contabilidad.form import ContabilidadForm, ActivoFijoForm
# Create your views here.

def index(request):
    return render(request,'mod_contabilidad/index.html')

def contabilidad(request):
    return render(request, 'mod_contabilidad/contabilidad.html')


class ActivoFijoCreate(CreateView):
    model = ActivoFijo
    form_class = ActivoFijoForm
    template_name = 'mod_contabilidad/activofijo_form.html'
    success_url = reverse_lazy('contabilidad_activos_fijos')

class ActivoFijoList(ListView):
	model = ActivoFijo
	template_name = 'mod_contabilidad/activofijo_list.html'


class ActivoFijoUpdate(UpdateView):
	model = ActivoFijo
	form_class = ActivoFijoForm
	template_name = 'mod_contabilidad/activofijo_form.html'
	success_url = reverse_lazy('contabilidad_activos_fijos')

class ActivoFijoDelete(DeleteView):
	model = ActivoFijo
	form_class = ActivoFijoForm
	template_name = 'mod_contabilidad/activofijo_delete.html'
	success_url = reverse_lazy('contabilidad_activos_fijos')