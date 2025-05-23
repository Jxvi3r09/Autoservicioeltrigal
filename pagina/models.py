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
    id = models.CharField(  # Changed from codigo_barras to id
        primary_key=True,
        max_length=50,
        verbose_name="Código de Barras"
    )
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    iva = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    cantidad_producto = models.IntegerField(default=0)
    fecha_vencimiento = models.DateField(null=True, blank=True)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'pagina_producto'
        
    def __str__(self):
        return f"{self.nombre} - {self.id}"

# COPIAS DE SEGURIDAD
class ConfiguracionRespaldo(models.Model):
    FRECUENCIAS = [
        ('diario', 'Diario'),
        ('semanal', 'Semanal'),
        ('mensual', 'Mensual'),
    ]

    frecuencia = models.CharField(max_length=10, choices=FRECUENCIAS, default='diario')
    hora = models.TimeField(default='02:00')
    cantidad = models.PositiveIntegerField(default=5)

    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.frecuencia} a las {self.hora} - mantener {self.cantidad}"

class Backup(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=50)
    tamano = models.CharField(max_length=20)
    estado = models.CharField(max_length=50, default='Completado')
    archivo = models.CharField(max_length=255)

    class Meta:
        ordering = ['-fecha']

    def __str__(self):
        return f"Backup {self.fecha.strftime('%Y-%m-%d %H:%M')} - {self.tipo}"

class Pedido(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('recibido', 'Recibido'),
        ('cancelado', 'Cancelado'),
    ]
    
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    fecha_entrega = models.DateField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    
    def __str__(self):
        return f"Pedido {self.id} - {self.proveedor.empresa}"

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.pedido.id} - {self.producto.nombre}"

class Venta(models.Model):
    fecha_venta = models.DateTimeField(auto_now_add=True)
    cliente = models.CharField(max_length=200, blank=True, null=True)  # Hacer opcional
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    vendedor = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Venta #{self.id} - {self.fecha_venta.strftime('%d/%m/%Y %H:%M')}"

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        # Calcular subtotal antes de guardar
        self.subtotal = self.cantidad * self.precio_unitario
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.venta.id} - {self.producto.nombre} x {self.cantidad}"



