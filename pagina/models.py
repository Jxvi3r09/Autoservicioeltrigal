from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import login
from django.shortcuts import render
from django.core.validators import RegexValidator
from django.db import models


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

    # Campos personalizados
    tipo_documento = models.CharField(
        max_length=2,
        choices=TIPOS_DOCUMENTO,
        default='CC'
    )
    numero_documento = models.CharField(
    max_length=20,
    unique=True,
    validators=[
        RegexValidator(
            regex='^[0-9]+$',
            message='El número de documento solo puede contener dígitos'
        )
    ],
    default='0000000000'  # Valor temporal por defecto
    )
    
    rol = models.CharField(
        max_length=20,
        choices=ROLES,
        default='empleado'
    )
    
    # Campo principal para el email (reemplaza el email por defecto)
    email = models.EmailField(
    max_length=254,
    unique=True,
    verbose_name="Correo electrónico",
    help_text="Ingrese su correo electrónico",
    blank=False,  # No permite valores en blanco
    null=False,   # No permite valores NULL
    error_messages={
        'unique': "Este correo electrónico ya está registrado.",
        'blank': "El correo electrónico es obligatorio.",
        'null': "El correo electrónico es obligatorio."
    }
    )

    imagen_perfil = models.ImageField(
      upload_to='perfiles/', blank=True, null=True)
    
    # # Mantenemos contacto como campo opcional si es necesario
    # contacto = models.CharField(
    #     max_length=50,
    #     blank=True,
    #     null=True,
    #     help_text="Número telefónico o contacto adicional"
    # )
    
    fecha_registro = models.DateTimeField(auto_now_add=True)

    # Configuración para usar email como identificador
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'  # Indica que este es el campo principal de email
    REQUIRED_FIELDS = ['email', 'numero_documento', 'rol']

    def __str__(self):
        return f"{self.username} - {self.email}"

    def save(self, *args, **kwargs):
        """Normaliza el email antes de guardar"""
        if self.email:
            self.email = self.email.lower().strip()
        super().save(*args, **kwargs)




class Proveedor(models.Model):
    nit_proveedor = models.CharField(max_length=20, unique=True)
    empresa = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=255)

    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.empresa} ({self.nit_proveedor})"
        
#Creacion de productos
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    iva = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    cantidad_entrada = models.IntegerField(default=0)
    cantidad_salida = models.IntegerField(default=0)
    fecha_vencimiento = models.DateField(null=True, blank=True)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre


