from django.db import models

# Create your models here.

class Giro(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=15)
    nombre = models.CharField(max_length=40)
    direccion = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    cred_disponible = models.IntegerField()
    habilitado = models.BooleanField()
    giros = models.ManyToManyField(Giro, through="Giro_cliente" )

class Giro_cliente(models.Model):
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, default=1)
    id_giro = models.ForeignKey(Giro, on_delete=models.CASCADE)

class Pago(models.Model):
    id = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    monto_cancelado = models.IntegerField()
    nombre = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    estado = models.BooleanField()






