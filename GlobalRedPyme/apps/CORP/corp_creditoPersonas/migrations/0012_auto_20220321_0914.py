# Generated by Django 3.1.7 on 2022-03-21 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corp_creditoPersonas', '0011_autorizacioncredito'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditopersonas',
            name='checkCedula',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='creditopersonas',
            name='checkManualPago',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='creditopersonas',
            name='checkPagare',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='creditopersonas',
            name='checkTablaAmortizacion',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='creditopersonas',
            name='codigoCliente',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='creditopersonas',
            name='codigoCorp',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='creditopersonas',
            name='montoVenta',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='creditopersonas',
            name='numeroFactura',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
