from django.db import models
from apps.mod_inventario.models import Producto,Categoria

from .validators import ValidateMayorCero


# Create your models here.

class Adquisicion(models.Model):
    ESTADOS= (
        ('pendiente','Pendiente'),
        ('entregada','Entregada'),
        ('pagado','Pagado'),
    )


    id = models.AutoField(primary_key=True)
    id_cat = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    id_prod = models.ManyToManyField(Producto, through='AdquisicionesProductos')
    precio_compra = models.PositiveIntegerField(validators=[ValidateMayorCero])
    estado = models.CharField(max_length=20, default='pendiente', choices=ESTADOS)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class AdquisicionesProductos(models.Model):
    id_adq = models.ForeignKey(Adquisicion, on_delete=models.CASCADE)
    id_prod = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(validators=[ValidateMayorCero])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Proveedor(models.Model):
    id = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=13, unique=True)
    nombre = models.CharField(max_length=20)
    direccion = models.CharField(max_length=30)
    telefono = models.CharField(max_length=10)
    email = models.CharField(max_length=30, default='N/A')
    estado = models.BooleanField(default=True)
    nom_cont = models.CharField(max_length=20)
    giro = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Orden_adq(models.Model):
    id = models.AutoField(primary_key=True)
    id_adq = models.ForeignKey(Adquisicion, on_delete=models.CASCADE)
    id_prov = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)