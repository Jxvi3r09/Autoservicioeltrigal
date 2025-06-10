from django import forms
from django.core.exceptions import ValidationError
from .models import Usuario  # Asegúrate de importar el modelo correcto
import re
from .models import Producto
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import validate_email
from .models import ConfiguracionRespaldo


# Recuperacion de contraseña
class CustomPasswordResetForm(PasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data.get('email', '').strip().lower()
        User = get_user_model()
        
        # Validación 1: Verificar que el email no esté vacío
        if not email:
            raise ValidationError("Por favor ingrese un correo electrónico.")
        
        # Validación 2: Verificar formato de email
        if '@' not in email:
            raise ValidationError("Ingrese una dirección de correo electrónico válida.")
        
        # Validación 3: Verificar existencia en la base de datos
        if not User.objects.filter(email__iexact=email).exists():
            raise ValidationError("No existe una cuenta asociada a este correo electrónico.")
        
        return email

class RegistroUsuarioForm(UserCreationForm):
    # Campos personalizados del modelo
    tipo_documento = forms.ChoiceField(
        choices=Usuario.TIPOS_DOCUMENTO,
        label="Tipo de Documento",
        initial='CC',
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    

    numero_documento = forms.CharField(
        max_length=20,
        label="Número de Documento",
        widget=forms.TextInput(attrs={
            'autocomplete': 'off',
            'placeholder': 'Ingrese solo números',
            'oninput': 'this.value = this.value.replace(/[^0-9]/g, "")'
        }),
        help_text="Solo números, sin puntos ni espacios"
    )

    def clean_numero_documento(self):
        data = self.cleaned_data['numero_documento']
        if not data.isdigit():
            raise forms.ValidationError("El número de documento solo puede contener números.")
        return data
    
    rol = forms.ChoiceField(
        choices=Usuario.ROLES,
        label="Rol",
        initial='empleado',
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = Usuario
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'tipo_documento',
            'numero_documento',
            'rol',
            'password1',
            'password2'
        ]
        labels = {
            'username': 'Nombre de usuario',
            'email': 'Correo electrónico',
            'first_name': 'Nombres',
            'last_name': 'Apellidos',
        }
        widgets = {
            'email': forms.EmailInput(attrs={'autocomplete': 'off'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalización de mensajes
        self.fields['password1'].help_text = "Mínimo 8 caracteres con números y letras."
        self.fields['password2'].help_text = "Repita la misma contraseña para verificación."
        
        # Estilo uniforme para campos
        for field in self.fields.values():
            if not isinstance(field.widget, forms.Select):
                field.widget.attrs.update({'class': 'form-control'})

    def clean_numero_documento(self):
        numero_documento = self.cleaned_data.get('numero_documento', '').strip()
        if not numero_documento:
            raise ValidationError("El número de documento es obligatorio.")
        
        if not numero_documento.isdigit():
            raise ValidationError("Solo se permiten caracteres numéricos.")
            
        if Usuario.objects.filter(numero_documento=numero_documento).exists():
            raise ValidationError("Este número de documento ya está registrado.")
            
        return numero_documento

    def clean_email(self):
        email = self.cleaned_data.get('email', '').lower().strip()
        
        try:
            validate_email(email)
        except ValidationError:
            raise ValidationError("Ingrese un correo electrónico válido.")
        
        if Usuario.objects.filter(email__iexact=email).exists():
            raise ValidationError("Este correo electrónico ya está registrado.")
            
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = user.email.lower().strip()  # Normalización
        
        if commit:
            user.save()
            self.save_m2m()  # Para relaciones many-to-many si las hubiera
            
        return user

from .models import Proveedor

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nit_proveedor', 'empresa', 'correo', 'telefono', 'direccion']


# inventario/forms.py
from django import forms
from .models import Producto, Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']
        widgets = {
    'nombre': forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Nombre de la categoría',
        'required': 'required'  # Esto lo hace obligatorio en HTML
    }),
}

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre'].strip().lower()  # Ignora mayúsculas/minúsculas y espacios
        if Categoria.objects.filter(nombre__iexact=nombre).exists():
            raise forms.ValidationError("Ya existe una categoría con ese nombre.")
        return nombre


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'categoria', 'precio', 'cantidad_producto', 'imagen']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'cantidad_producto': forms.NumberInput(attrs={'class': 'form-control'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'})
        }

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if (precio <= 0):
            raise forms.ValidationError('El precio debe ser mayor que 0')
        return precio

    def clean_cantidad_producto(self):
        cantidad = self.cleaned_data.get('cantidad_producto')
        if (cantidad < 0):
            raise forms.ValidationError('La cantidad no puede ser negativa')
        return cantidad

class ConfiguracionRespaldoForm(forms.Form):
    FRECUENCIA_CHOICES = [
        ('diario', 'Diario'),
        ('semanal', 'Semanal'),
        ('mensual', 'Mensual'),
    ]
    
    frecuencia = forms.ChoiceField(
        choices=FRECUENCIA_CHOICES,
        label='Frecuencia'
    )
    
    hora = forms.TimeField(
        label='Hora',
        widget=forms.TimeInput(attrs={'type': 'time'})
    )
    
    cantidad = forms.IntegerField(
        label='Cantidad de respaldos',
        min_value=1,
        max_value=30,
        initial=7
    )

class RespaldosForm(forms.Form):
    FRECUENCIAS = [
        ('diario', 'Diario'),
        ('semanal', 'Semanal'),
        ('mensual', 'Mensual')
    ]
    
    frecuencia = forms.ChoiceField(
        choices=FRECUENCIAS,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    hora = forms.TimeField(
        widget=forms.TimeInput(attrs={
            'class': 'form-control',
            'type': 'time'
        })
    )
    
    cantidad = forms.IntegerField(
        min_value=1,
        max_value=30,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

class RespaldoForm(forms.Form):
    FRECUENCIA_CHOICES = [
        ('diario', 'Diario'),
        ('semanal', 'Semanal'),
        ('mensual', 'Mensual')
    ]
    
    frecuencia = forms.ChoiceField(
        choices=FRECUENCIA_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Frecuencia de respaldo'
    )
    
    hora = forms.TimeField(
        widget=forms.TimeInput(attrs={
            'class': 'form-control',
            'type': 'time'
        }),
        initial='02:00'
    )
    
    cantidad = forms.IntegerField(
        min_value=1,
        max_value=30,
        initial=7,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )