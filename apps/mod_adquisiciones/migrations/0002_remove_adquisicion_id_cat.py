# Generated by Django 2.1.2 on 2018-10-31 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mod_adquisiciones', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adquisicion',
            name='id_cat',
        ),
    ]
