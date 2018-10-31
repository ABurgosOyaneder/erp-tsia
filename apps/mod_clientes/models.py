from django.db import models

# Create your models here.

class Giro(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)

class Giro_cliente(models.Model):
    id = models.AutoField(primary_key=True)
    id_giro = models.ForeignKey(Giro, on_delete=models.CASCADE)

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=15)
    nombre = models.CharField(max_length=40)
    direccion = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    cred_disponible = models.IntegerField()
    habilitado = models.BooleanField()
    id_giro = models.ForeignKey(Giro_cliente, on_delete=models.CASCADE)
