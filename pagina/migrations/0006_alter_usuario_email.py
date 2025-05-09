# Generated by Django 5.1.6 on 2025-05-09 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0005_fix_duplicate_emails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(error_messages={'blank': 'El correo electrónico es obligatorio.', 'null': 'El correo electrónico es obligatorio.', 'unique': 'Este correo electrónico ya está registrado.'}, help_text='Ingrese su correo electrónico', max_length=254, unique=True, verbose_name='Correo electrónico'),
        ),
    ]
