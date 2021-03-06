# Generated by Django 3.1.7 on 2022-02-22 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mdp_categorias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategorias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('codigoSubCategoria', models.CharField(max_length=255)),
                ('descripcion', models.TextField(null=True)),
                ('estado', models.CharField(default='Inactivo', max_length=150)),
                ('empresa_id', models.CharField(blank=True, max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('state', models.SmallIntegerField(default=1)),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mdp_categorias.categorias')),
            ],
        ),
    ]
