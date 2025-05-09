from django import forms
from django.core.exceptions import ValidationError
from .models import Usuario  # Asegúrate de importar el modelo correcto
import re
from .models import Producto
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import validate_email


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
        widget=forms.TextInput(attrs={'autocomplete': 'off'}),
        help_text="Solo números, sin puntos ni espacios"
    )
    
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
        widgets = {
            'nit_proveedor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NIT del proveedor'}),
            'empresa': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la empresa'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono de contacto'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección'}),
        }



# inventario/forms.py
from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre','precio','cantidad_entrada','fecha_vencimiento']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'id_nombre',
                'placeholder': 'Nombre del producto',
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'form-control',
                'id': 'id_precio',
                'step': '0.01',
                'placeholder': '0.00',
            }),
            'cantidad_entrada': forms.NumberInput(attrs={
                'class': 'form-control',
                'id': 'id_cantidad_entrada',
                'placeholder': '0',
            }),
            'fecha_vencimiento': forms.DateInput(attrs={
                'class': 'form-control',
                'id': 'id_fecha_vencimiento',
                'type': 'date',
            }),
        }

