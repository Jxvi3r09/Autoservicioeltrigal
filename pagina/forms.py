from django import forms
from django.core.exceptions import ValidationError
from .models import Usuario  # Asegúrate de importar el modelo correcto
import re
from .models import Producto


#Registro de usuarios
class RegistroUsuarioForm(forms.ModelForm):
    contacto = forms.CharField(
        max_length=50,
        required=True,
        label="Correo electrónico o Número de teléfono",
        help_text="Ingrese su correo o número telefónico"
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "id": "password"}),
        label="Contraseña",
        help_text="Debe contener al menos 8 caracteres, incluyendo números y letras."
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "id": "confirm_password"}),
        label="Confirmar Contraseña"
    )

    class Meta:
        model = Usuario
        fields = [
            "tipo_documento", "numero_documento", "first_name", "last_name",
            "rol", "contacto", "username", "password"
        ]
        labels = {
            "first_name": "Nombres",
            "last_name": "Apellidos",
            "tipo_documento": "Tipo de Documento",
            "numero_documento": "Número de Documento",
            "rol": "Rol",
            "username": "Usuario",
            "password": "Contraseña",
        }
        widgets = {
            "username": forms.TextInput(attrs={"autocomplete": "off"}),
            "first_name": forms.TextInput(attrs={"autocomplete": "off"}),
            "last_name": forms.TextInput(attrs={"autocomplete": "off"}),
            "numero_documento": forms.TextInput(attrs={"autocomplete": "off"}),
            "contacto": forms.TextInput(attrs={"autocomplete": "off", "id": "contacto"}),
        }

    def clean_numero_documento(self):
        numero_documento = self.cleaned_data.get("numero_documento")
        if not numero_documento:
            raise ValidationError("Este campo es obligatorio.")
        if not numero_documento.isdigit():
            raise ValidationError("El número de documento solo puede contener números.")
        return numero_documento

    def clean_contacto(self):
        contacto = self.cleaned_data.get("contacto", "").strip()
        contacto_normalizado = re.sub(r"[()\s\-]", "", contacto)

        email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        phone_regex = r"^\+?[0-9]{7,15}$"

        if re.fullmatch(email_regex, contacto):
            return contacto  # Correo válido
        if re.fullmatch(phone_regex, contacto_normalizado):
            return contacto_normalizado  # Teléfono válido (normalizado)
        
        raise ValidationError("Ingrese un correo electrónico válido o un número de teléfono válido.")

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if Usuario.objects.filter(username=username).exists():
            raise ValidationError("El nombre de usuario ya está en uso.")
        return username

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if len(password) < 8 or not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password):
            raise ValidationError("La contraseña debe tener al menos 8 caracteres y contener números y letras.")
        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error("confirm_password", "Las contraseñas no coinciden.")




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

