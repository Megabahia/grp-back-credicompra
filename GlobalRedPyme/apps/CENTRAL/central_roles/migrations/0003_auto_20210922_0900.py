# Generated by Django 3.1.7 on 2021-09-22 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('central_roles', '0002_rolesusuarios'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rolesusuarios',
            old_name='role',
            new_name='rol',
        ),
        migrations.AlterField(
            model_name='roles',
            name='descripcion',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
