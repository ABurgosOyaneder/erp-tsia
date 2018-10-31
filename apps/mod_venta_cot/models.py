from django.db import models
from apps.mod_inventario.models import Producto
from apps.mod_clientes.models import Cliente

# Create your models here.

class Medio_pago(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    descuento = models.FloatField()

class Producto_cotizacion(models.Model):
    id = models.AutoField(primary_key=True)
    id_prod = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.IntegerField()

class Cotizacion(models.Model):
    id = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_prod_cot = models.ForeignKey(Producto_cotizacion, on_delete=models.CASCADE)
    id_medio = models.ForeignKey(Medio_pago, on_delete=models.CASCADE)
    fecha_vencimiento = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    subtotal = models.IntegerField()
    impuestos = models.IntegerField()
    descuento = models.FloatField()
    estado = models.BooleanField()