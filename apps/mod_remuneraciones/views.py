from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from apps.mod_remuneraciones.models import Box

# Create your views here.
def index(request):
    return render(request,'mod_remuneraciones/index.html')

class BoxList(ListView):
    model = Box

class BoxView(DetailView):
    model = Box

class BoxCreate(CreateView):
    model = Box
    fields = ['nombre']
    success_url = reverse_lazy('box_list')

class BoxUpdate(UpdateView):
    model = Box
    fields = ['nombre']
    success_url = reverse_lazy('box_list')

class BoxDelete(DeleteView):
    model = Box
    success_url = reverse_lazy('box_list')
