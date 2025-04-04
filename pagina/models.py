from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

#Creacion del usuario
class Usuario(AbstractUser):
    TIPOS_DOCUMENTO = [
        ('CC', 'Cédula de Ciudadanía'),
        ('TI', 'Tarjeta de Identidad'),
        ('CE', 'Cédula de Extranjería'),
        ('PP', 'Pasaporte'),
    ]
    
    ROLES = [
        ('administrador', 'Administrador'),
        ('empleado', 'Empleado'),
    ]
#Datos de la base de datos
    id = models.AutoField(primary_key=True)  # ID automático
    tipo_documento = models.CharField(max_length=2, choices=TIPOS_DOCUMENTO, default='CC')
    numero_documento = models.CharField(max_length=20, unique=True)
    rol = models.CharField(max_length=20, choices=ROLES, default='empleado')
    contacto = models.CharField(max_length=50, help_text="Ingrese su correo electrónico o número de teléfono")

    def __str__(self):
        return f"{self.username} - {self.rol}"

#Creacion de proveedor
class Proveedor(models.Model):
    nit_proveedor = models.CharField(max_length=20, unique=True, verbose_name="NIT Proveedor")
    empresa = models.CharField(max_length=100, verbose_name="Empresa")
    correo = models.EmailField(max_length=100, verbose_name="Correo Electrónico")
    telefono = models.BigIntegerField(verbose_name="Teléfono")
    direccion = models.CharField(max_length=255, verbose_name="Dirección")

    def __str__(self):
        # Representación en formato string del proveedor, por ejemplo, por el nombre de la empresa
        return self.empresa

    class Meta:
        # Nombre de la tabla en la base de datos y ordenamiento
        db_table = 'proveedores'
        ordering = ['empresa']
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'