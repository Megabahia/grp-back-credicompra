# Generated by Django 3.1.7 on 2022-03-29 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corp_creditoArchivos', '0002_auto_20220328_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='preaprobados',
            name='estado',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
