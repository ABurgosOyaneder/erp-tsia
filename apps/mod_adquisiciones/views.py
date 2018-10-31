from django.shortcuts import render
from django.views.generic import ListView

from apps.mod_adquisiciones.models import Adquisicion , Ingreso , Proveedor , Orden_adq

def index(request):
    return render(request,'mod_adquisiciones/index.html')

def adquisiciones(request):
    return render(request,'mod_adquisiciones/adquisiciones.html')
    
def compras(request):
    return render(request,'mod_adquisiciones/compras.html')

class AdquisicionesList(ListView):
	model = Adquisicion
	template_name = 'mod_adquisiciones/adquisiciones.html'