from django.db import models
from django.urls import reverse

# Create your models here.

class Caja_de_compensacion(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('caja_edit', kwargs={'pk': self.pk})

class Mutual(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Banco(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Previsionsalud(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    tipo = models.CharField(max_length=20)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Prevision(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    porcentaje_descuento = models.FloatField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Tipo_descuento_haber(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    positivo = models.BooleanField()
    tipo = models.CharField(max_length=30)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Funcionario(models.Model):
    id = models.AutoField(primary_key=True)
    id_prev_sal = models.ForeignKey(Previsionsalud, on_delete=models.CASCADE)
    id_prev = models.ForeignKey(Prevision, on_delete=models.CASCADE)
    id_banco = models.ForeignKey(Banco, on_delete=models.CASCADE)
    rut = models.CharField(max_length=15)
    nombres = models.CharField(max_length=40)
    paterno = models.CharField(max_length=40)
    materno = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    edad = models.IntegerField()
    estado_civil = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=20)
    mail = models.CharField(max_length=30)
    nacionalidad = models.CharField(max_length=30)
    telefono = models.CharField(max_length=15)
    sueldobase = models.IntegerField()
    plansalud = models.IntegerField()
    vendedor = models.BooleanField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Liquidacion(models.Model):
    id = models.AutoField(primary_key=True)
    id_funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    sueldo_bruto = models.IntegerField()
    total_contabilidad = models.IntegerField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Descuento_haber(models.Model):
    id = models.AutoField(primary_key=True)
    id_funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    frecuente = models.BooleanField()
    monto = models.IntegerField()
    id_tipo = models.ForeignKey(Tipo_descuento_haber, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)