from django.db import models
from apps.mod_cotizaciones.models import Cotizacion

# Create your models here.
class Cargo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    valor = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    id_cotizacion = models.ForeignKey(Cotizacion, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    total = models.IntegerField()
    estado = models.CharField(max_length=20)
    cargos = models.ManyToManyField(Cargo, through="Cargo_venta")

class Cargo_venta(models.Model):
    id_venta = models.ForeignKey(Venta, on_delete=models.CASCADE, default=1)
    id_cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Factura(models.Model):
    id = models.AutoField(primary_key=True)
    id_venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    vencimiento = models.DateField()