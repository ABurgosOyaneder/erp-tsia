from django.db import models
from apps.mod_inventario.models import Producto
from apps.mod_clientes.models import Cliente

# Create your models here.

class Medio_pago(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    descuento = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Cotizacion(models.Model):
    id = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_medio = models.ForeignKey(Medio_pago, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto, through="Producto_cotizacion")
    fecha_vencimiento = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    subtotal = models.IntegerField()
    impuestos = models.IntegerField()
    descuento = models.FloatField()
    estado = models.BooleanField()

class Producto_cotizacion(models.Model):
    id_prod = models.ForeignKey(Producto, on_delete=models.CASCADE)
    id_cot = models.ForeignKey(Cotizacion, on_delete=models.CASCADE, default=1)
    cantidad = models.IntegerField()
    precio_unitario = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

