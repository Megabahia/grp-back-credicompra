# Generated by Django 3.1.7 on 2022-01-18 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('central_facturas', '0002_facturas_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='facturas',
            name='atencion',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='facturas',
            name='calificacion',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='facturas',
            name='observaciones',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='facturas',
            name='pais',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='CalificarCompras',
        ),
    ]
