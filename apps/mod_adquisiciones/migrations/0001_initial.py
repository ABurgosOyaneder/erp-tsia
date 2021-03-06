# Generated by Django 2.1.2 on 2018-10-30 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mod_inventario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adquisicion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('precio_compra', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('id_cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mod_inventario.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Ingreso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('precio_compra', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('id_adq', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mod_adquisiciones.Adquisicion')),
                ('id_prod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mod_inventario.Producto')),
            ],
        ),
        migrations.CreateModel(
            name='Orden_adq',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('precio_compra', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('id_adq', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mod_adquisiciones.Adquisicion')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rut', models.CharField(max_length=13, unique=True)),
                ('nombre', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=10)),
                ('nom_cont', models.CharField(max_length=20)),
                ('giro', models.CharField(max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='orden_adq',
            name='id_prov',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mod_adquisiciones.Proveedor'),
        ),
        migrations.AddField(
            model_name='adquisicion',
            name='id_prod',
            field=models.ManyToManyField(through='mod_adquisiciones.Ingreso', to='mod_inventario.Producto'),
        ),
    ]
