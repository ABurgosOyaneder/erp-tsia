from django.db import models

# Create your models here.

class Categoria(models.Model):
    id = models.AutoField(primary_key = True)
    descripcion = models.CharField(max_length = 20)

class ActivoFijo(models.Model):
    id = models.AutoField(primary_key = True)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=20)
    depreciacion = models.PositiveIntegerField()
    costo = models.PositiveIntegerField()
    fecha_adq = models.DateField()
    fecha_lim = models.DateField()