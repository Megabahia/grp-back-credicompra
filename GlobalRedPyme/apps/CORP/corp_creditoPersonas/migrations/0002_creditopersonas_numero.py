# Generated by Django 3.1.7 on 2021-12-22 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corp_creditoPersonas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditopersonas',
            name='numero',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
