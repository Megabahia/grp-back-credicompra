# Generated by Django 3.1.7 on 2022-04-06 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Correos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaRegistro', models.DateField(auto_now_add=True)),
                ('correo', models.EmailField(max_length=255)),
                ('correoValido', models.BooleanField(default=False)),
                ('codigoValido', models.BooleanField(default=False)),
                ('accedio', models.BooleanField(default=False)),
                ('codigo', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('state', models.SmallIntegerField(default=1)),
            ],
        ),
    ]
