# Generated by Django 3.1.7 on 2021-10-01 15:34

import apps.CENTRAL.central_productos.models
from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('nombre', models.TextField(max_length=200)),
                ('marca', models.CharField(max_length=255)),
                ('imagen', models.FileField(blank=True, null=True, upload_to=apps.CENTRAL.central_productos.models.upload_path)),
                ('precioNormal', models.FloatField()),
                ('precioSupermonedas', models.CharField(max_length=200)),
                ('efectivo', models.FloatField()),
                ('codigoQR', models.CharField(blank=True, max_length=200, null=True)),
                ('cantidad', models.IntegerField()),
                ('empresa_id', models.CharField(max_length=200)),
                ('tipo', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('state', models.SmallIntegerField(default=1)),
            ],
        ),
    ]
