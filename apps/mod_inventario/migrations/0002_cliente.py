# Generated by Django 2.1.2 on 2018-10-27 01:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mod_inventario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=12)),
                ('nombre', models.CharField(max_length=20)),
                ('prod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mod_inventario.Item')),
            ],
        ),
    ]
