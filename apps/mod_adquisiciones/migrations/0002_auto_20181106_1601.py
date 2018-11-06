# Generated by Django 2.1.2 on 2018-11-06 19:01

import apps.mod_adquisiciones.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mod_inventario', '0001_initial'),
        ('mod_adquisiciones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdquisicionesProductos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(validators=[apps.mod_adquisiciones.validators.ValidateMayorCero])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='ingreso',
            name='id_adq',
        ),
        migrations.RemoveField(
            model_name='ingreso',
            name='id_prod',
        ),
        migrations.RemoveField(
            model_name='adquisicion',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='orden_adq',
            name='precio_compra',
        ),
        migrations.AddField(
            model_name='adquisicion',
            name='estado',
            field=models.CharField(default='pendiente', max_length=20),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='email',
            field=models.CharField(default='N/A', max_length=30),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='adquisicion',
            name='id_prod',
            field=models.ManyToManyField(through='mod_adquisiciones.AdquisicionesProductos', to='mod_inventario.Producto'),
        ),
        migrations.AlterField(
            model_name='adquisicion',
            name='precio_compra',
            field=models.PositiveIntegerField(validators=[apps.mod_adquisiciones.validators.ValidateMayorCero]),
        ),
        migrations.DeleteModel(
            name='Ingreso',
        ),
        migrations.AddField(
            model_name='adquisicionesproductos',
            name='id_adq',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mod_adquisiciones.Adquisicion'),
        ),
        migrations.AddField(
            model_name='adquisicionesproductos',
            name='id_prod',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mod_inventario.Producto'),
        ),
    ]
