# Generated by Django 3.1.7 on 2021-12-20 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas_personas', '0003_auto_20211007_0902'),
    ]

    operations = [
        migrations.AddField(
            model_name='personas',
            name='direccion',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='personas',
            name='pais',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='personas',
            name='telefono',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='personas',
            name='apellidos',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='personas',
            name='genero',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='personas',
            name='identificacion',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='personas',
            name='nombres',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
