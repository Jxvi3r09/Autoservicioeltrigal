from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class UsuarioAdmin(UserAdmin):
    list_display = ("username", "first_name", "last_name", "email", "rol", "numero_documento")
    search_fields = ("username", "first_name", "last_name", "email", "numero_documento")
    list_filter = ("rol", "is_active", "is_staff")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Información Personal", {"fields": ("first_name", "last_name", "email", "contacto")}),
        ("Detalles de Usuario", {"fields": ("tipo_documento", "numero_documento", "rol")}),
        ("Permisos", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Fechas Importantes", {"fields": ("last_login", "date_joined")}),
    )

admin.site.register(Usuario, UsuarioAdmin)
