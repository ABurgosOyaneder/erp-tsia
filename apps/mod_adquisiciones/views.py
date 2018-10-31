from django.shortcuts import render


def index(request):
    return render(request,'mod_adquisiciones/index.html')
def adquisiciones(request):
    return render(request,'mod_adquisiciones/adquisiciones.html')
def compras(request):
    return render(request,'mod_adquisiciones/compras.html')
