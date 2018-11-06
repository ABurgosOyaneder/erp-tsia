from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django import forms
from mod_facturacion.models import Factura


class ListaDeFacturas(ListView):
    model = Factura


class FacturaForm(forms.ModelForm):

    class Meta:
        model = Factura
        fields =  ['nombre', 'fecha',  
              'precio', 'iva', 'total',]
        widgets = {
            'fecha' : forms.DateInput(),
        }

        
class CrearFactura(CreateView):
    model = Factura
    # fields = ['nombre', 'fecha', 
    #         'precio', 'iva', 'total']
    form_class = FacturaForm
    success_url = reverse_lazy('facturacion:lista_facturas')


class ActualizarFactura(UpdateView):
    model = Factura
    fields = ['nombre', 'fecha', 
            'precio', 'iva', 'total']
    success_url = reverse_lazy('facturacion:lista_facturas')

class BorrarFactura(DeleteView):
    model = Factura
    success_url = reverse_lazy('facturacion:lista_facturas')

# class FacturaForm(forms.Form):
#     nombre = forms.CharField()
#     fecha = forms.DateTimeField(widget=forms.SelectDateWidget)
#     No estoy seguro si tienen un contrato de por medio HELP FELIPE
#     contrato = forms.ModelChoiceField(queryset=Contrato.objects.all())
#     precio = forms.DecimalField(validators=[])
#     iva = forms.CharField(disabled=True, initial="21%")
#     total = forms.DecimalField(disabled=True, initial=precio)