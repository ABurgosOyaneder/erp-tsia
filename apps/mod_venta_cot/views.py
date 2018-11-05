from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'mod_venta_cot/index.html')

def cotizacion(request):
    return render(request,'mod_venta_cot/cotizacion.html')

def venta(request):
    return render(request,'mod_venta_cot/venta.html')        