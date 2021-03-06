# Generated by Django 2.1.2 on 2018-10-31 02:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rut', models.CharField(max_length=15)),
                ('nombre', models.CharField(max_length=40)),
                ('direccion', models.CharField(max_length=50)),
                ('correo', models.CharField(max_length=50)),
                ('cred_disponible', models.IntegerField()),
                ('habilitado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Giro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Giro_cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('id_giro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mod_clientes.Giro')),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='id_giro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mod_clientes.Giro_cliente'),
        ),
    ]
