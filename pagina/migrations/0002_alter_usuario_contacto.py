# Generated by Django 5.1.6 on 2025-05-08 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='contacto',
            field=models.EmailField(help_text='Ingrese su correo electrónico', max_length=254, unique=True),
        ),
    ]
