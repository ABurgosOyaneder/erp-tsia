from django.db import models
from apps.mod_inventario.models import Producto
from apps.mod_clientes.models import Cliente
from apps.mod_remuneraciones.models import Funcionario

# Create your models here.
class Cargo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    valor = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Medio_pago(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    descuento = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_vendedor = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    id_medio = models.ForeignKey(Medio_pago, on_delete=models.CASCADE)
    total = models.IntegerField()
    estado = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20, default="Cotizacion")
    productos = models.ManyToManyField(Producto, through="Ven_prod")
    cargos = models.ManyToManyField(Cargo, through="Cargo_venta")

class Ven_prod(models.Model):
    id_prod = models.ForeignKey(Producto, on_delete=models.CASCADE)
    id_venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    precio = models.IntegerField()
    cantidad = models.IntegerField()
    comision = models.IntegerField(default=0)

class Cargo_venta(models.Model):
    id_venta = models.ForeignKey(Venta, on_delete=models.CASCADE, default=1)
    id_cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Factura(models.Model):
    id = models.AutoField(primary_key=True)
    id_venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    deuda_pendiente = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    vencimiento = models.DateField()