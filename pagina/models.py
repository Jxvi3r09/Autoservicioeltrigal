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
