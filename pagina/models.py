from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import login
from django.shortcuts import render



from django.contrib.auth.models import AbstractUser
from django.db import models

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

    id = models.AutoField(primary_key=True)
    tipo_documento = models.CharField(max_length=2, choices=TIPOS_DOCUMENTO, default='CC')
    numero_documento = models.CharField(max_length=20, unique=True, blank=True, null=True)
    rol = models.CharField(max_length=20, choices=ROLES, default='empleado')
    contacto = models.CharField(max_length=50, help_text="Ingrese su correo electrónico o número de teléfono")

    # Configuración para el modelo personalizado
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['numero_documento', 'rol', 'contacto']

    def __str__(self):
        return f"{self.username} - {self.rol}"


# Creación de proveedor
class Proveedor(models.Model):
    nit_proveedor = models.CharField(max_length=20, unique=True, verbose_name="NIT Proveedor")
    empresa = models.CharField(max_length=100, verbose_name="Empresa")
    correo = models.EmailField(max_length=100, verbose_name="Correo Electrónico")
    telefono = models.BigIntegerField(verbose_name="Teléfono")
    direccion = models.CharField(max_length=255, verbose_name="Dirección")

    def __str__(self):
        # Representación en formato string del proveedor
        return self.empresa

    class Meta:
        # Nombre de la tabla en la base de datos y ordenamiento
        db_table = 'proveedores'
        ordering = ['empresa']
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        
#Creacion de productos
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    codigo_barras = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    iva = models.DecimalField(max_digits=5, decimal_places=2)
    cantidad_entrada = models.IntegerField(default=0)
    cantidad_salida = models.IntegerField(default=0)
    fecha_vencimiento = models.DateField(null=True, blank=True)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nombre