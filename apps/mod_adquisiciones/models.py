from django.db import models
from apps.mod_inventario.models import Producto,Categoria

# Create your models here.

class Adquisicion(models.Model):
    id = models.AutoField(primary_key=True)
    id_cat = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    id_prod = models.ManyToManyField(Producto, through='Ingreso')
    cantidad = models.IntegerField()
    precio_compra = models.IntegerField()

class Ingreso(models.Model):
    id_adq = models.ForeignKey(Adquisicion, on_delete=models.CASCADE)
    id_prod = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_compra = models.IntegerField()

class Proveedor(models.Model):
    id = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=13, unique=True)
    nombre = models.CharField(max_length=20)
    direccion = models.CharField(max_length=30)
    telefono = models.CharField(max_length=10)
    nom_cont = models.CharField(max_length=20)
    giro = models.CharField(max_length=20)

class Orden_adq(models.Model):
    id = models.AutoField(primary_key=True)
    id_adq = models.ForeignKey(Adquisicion, on_delete=models.CASCADE)
    id_prov = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    precio_compra = models.IntegerField()