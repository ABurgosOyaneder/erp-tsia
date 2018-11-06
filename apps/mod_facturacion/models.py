from django.db import models
from apps.mod_venta_cot.models import Venta
from django.urls import reverse
import datetime
# Create your models here.

class Factura(models.Model):
    id = models.AutoField(primary_key=True)
    id_venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    iva = models.PositiveSmallIntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    vencimiento = models.DateField()

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('facturacion:editar_factura', kwargs={'pk': self.pk})