# Generated by Django 3.1.7 on 2022-02-11 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corp_creditoPersonas', '0003_auto_20220209_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditopersonas',
            name='concepto',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='creditopersonas',
            name='tipoCredito',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='creditopersonas',
            name='tomarSolicitud',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
