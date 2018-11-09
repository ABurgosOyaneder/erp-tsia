from django.db import models
from apps.mod_inventario.models import Producto

# Create your models here.
class Proveedor(models.Model):
    id = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=13, unique=True)
    nombre = models.CharField(max_length=20)
    direccion = models.CharField(max_length=30)
    telefono = models.CharField(max_length=10)
    nom_cont = models.CharField(max_length=20)
    giro = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class OrdenAdq(models.Model):
    id = models.AutoField(primary_key=True)
    id_prov = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto, through="Ingreso")
    precio_compra = models.IntegerField()
    cantidad = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Ingreso(models.Model):
    id_adq = models.ForeignKey(OrdenAdq, on_delete=models.CASCADE)
    id_prod = models.ForeignKey(Producto, on_delete=models.CASCADE)
    precio_compra = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)