from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def index(request):
    return render(request,'core/index.html')

def prueba(request):
    data = {
        'labels': ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"],
        'datos':[{
            'label':'Ventas por mes en $',
            'data':[125000, 192000, 303000, 51200, 234000, 30000],
            'backgroundColor': [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            'borderColor': [
                'rgba(255,99,132,1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            'borderWidth': 2
        }]
    }
    return JsonResponse(data)
