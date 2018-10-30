from django.shortcuts import render

def index(request):
    return render(request,'mod_adquisiciones/index.html')