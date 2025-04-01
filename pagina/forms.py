from django import forms
from django.core.exceptions import ValidationError
from .models import Usuario  # Asegúrate de importar el modelo correcto
import re

class RegistroUsuarioForm(forms.ModelForm):
    contacto = forms.CharField(
        max_length=50,
        required=True,
        label="Correo electrónico o Número de teléfono",
        help_text="Ingrese su correo o número telefónico"
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        label="Contraseña",
        help_text="Debe contener al menos 8 caracteres, incluyendo números y letras."
    )

    class Meta:
        model = Usuario  # Usa tu modelo de usuario personalizado
        fields = ["tipo_documento", "numero_documento", "first_name", "last_name", "rol", "contacto", "username", "password"]
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
            "contacto": forms.TextInput(attrs={"autocomplete": "off"}),
        }

    def clean_numero_documento(self):
        numero_documento = self.cleaned_data.get("numero_documento")
        if not numero_documento.isdigit():
            raise ValidationError("El número de documento solo puede contener números.")
        return numero_documento

    def clean_contacto(self):
        contacto = self.cleaned_data.get("contacto")
        email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        phone_regex = r"^\+?[0-9]{7,15}$"

        if not re.match(email_regex, contacto) and not re.match(phone_regex, contacto):
            raise ValidationError("Ingrese un correo electrónico válido o un número de teléfono válido.")
        return contacto

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if Usuario.objects.filter(username=username).exists():  # Se cambió User por Usuario
            raise ValidationError("El nombre de usuario ya está en uso.")
        return username

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if len(password) < 8 or not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password):
            raise ValidationError("La contraseña debe tener al menos 8 caracteres y contener números y letras.")
        return password

from django import forms
from .models import Proveedor

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nit_proveedor', 'empresa', 'correo', 'telefono', 'direccion']
        widgets = {
            'direccion': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Ingrese la dirección completa'}),
        }

    # Validación adicional si es necesario (opcional)
    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if len(str(telefono)) < 10:
            raise forms.ValidationError("El teléfono debe tener al menos 10 dígitos.")
        return telefono
