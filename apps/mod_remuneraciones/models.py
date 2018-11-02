from django.db import models

# Create your models here.

class Box(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('box_edit', kwargs={'pk': self.pk})

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

class Empresa(models.Model):
    id = models.AutoField(primary_key=True)
    id_box = models.ForeignKey(Box, on_delete=models.CASCADE)
    id_mutual = models.ForeignKey(Mutual, on_delete=models.CASCADE)
    id_banco = models.ForeignKey(Banco, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)
    rut = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    telefono = models.CharField(max_length=12)
    sitio = models.URLField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Previsionsalud(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    porcentaje_descuento = models.FloatField()
    tipo = models.CharField(max_length=20)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Prevision(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    porcentaje_descuento = models.FloatField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Horas(models.Model):
    id = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()
    historico = models.BooleanField()
    monto = models.IntegerField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Salario(models.Model):
    id = models.AutoField(primary_key=True)
    detalle = models.CharField(max_length=30)
    frecuente = models.BooleanField()
    historico = models.BooleanField()
    monto = models.IntegerField()
    tipo = models.CharField(max_length=30)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Prestamo(models.Model):
    id = models.AutoField(primary_key=True)
    cantidad_total = models.IntegerField()
    cuotas = models.IntegerField()
    cuotas_restantes = models.IntegerField()
    historico = models.BooleanField()
    saldo = models.IntegerField()
    valorcuota = models.IntegerField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Descuento(models.Model):
    id = models.AutoField(primary_key=True)
    detalle = models.CharField(max_length=30)
    frecuente = models.BooleanField()
    historico = models.BooleanField()
    monto = models.IntegerField()
    tipo = models.CharField(max_length=20)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Liquidacion(models.Model):
    id = models.AutoField(primary_key=True)
    id_hora = models.ForeignKey(Horas, on_delete=models.CASCADE)
    id_salario = models.ForeignKey(Salario, on_delete=models.CASCADE)
    id_prestamo = models.ForeignKey(Prestamo, on_delete=models.CASCADE)
    id_descuento = models.ForeignKey(Descuento, on_delete=models.CASCADE)
    sueldo_bruto = models.IntegerField()
    sueldo_liquido = models.IntegerField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Ficha_Trabajador(models.Model):
    id = models.AutoField(primary_key=True)
    id_prev_sal = models.ForeignKey(Previsionsalud, on_delete=models.CASCADE)
    id_prev = models.ForeignKey(Prevision, on_delete=models.CASCADE)
    id_empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    id_liquidacion = models.ForeignKey(Liquidacion, on_delete=models.CASCADE)
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

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)