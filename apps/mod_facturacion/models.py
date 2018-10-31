from django.db import models
from apps.mod_venta_cot.models import Venta

# Create your models here.

class Factura(models.Model):
    id = models.AutoField(primary_key=True)
    id_venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    vencimiento = models.DateField()