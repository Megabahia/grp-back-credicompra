# Generated by Django 3.1.7 on 2022-01-04 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas_personas', '0004_auto_20211220_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='personas',
            name='nombresCompleto',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
