from django.db import models

# Create your models here.
class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=100)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Producto(models.Model):
    id_prod = models.AutoField(primary_key=True)
    id_cat = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=20)
    cod_barra = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    precio_compra = models.IntegerField()
    precio_venta = models.IntegerField()
    stock = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)