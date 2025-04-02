from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import RegistroUsuarioForm  # Asegúrate de importar el formulario
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.views import PasswordResetView



def principal(request):
    return render(request, "paginas/principal.html")

def index(request):
    return render(request, "paginas/index.html")

def inventario(request):
    return render(request, "sistema/inventario.html")

def administrador(request):
    return render(request, "sistema/administrador.html")

def proveedores(request):
    return render(request, "sistema/proveedores.html")

def agregar_proveedores(request):
    return render(request, "sistema/agregar_proveedores.html")

def modal_inicio(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()

        # Verificar si los campos están vacíos
        if not username or not password:
            messages.error(request, "⚠️ Todos los campos son obligatorios.")
            return redirect("inicio")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"✅ Bienvenido {user.first_name} {user.last_name}!")
            return redirect("inventario")  # Redirige a inicio_inventario
        else:
            messages.error(request, "❌ Usuario o contraseña incorrectos.")

    return render(request, "paginas/inicio.html")

def registro(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)  # No guardamos aún
            usuario.set_password(form.cleaned_data["password"])  # Encriptamos la contraseña
            usuario.save()  # Ahora sí guardamos
            login(request, usuario)

            form = RegistroUsuarioForm()  # Limpia los campos estableciendo un nuevo formulario vacío
            return render(request, "paginas/registrate.html", {"form": form})  # Recarga con el formulario vacío
    else:
        form = RegistroUsuarioForm()  # Se ejecuta solo si el método NO es POST

    return render(request, "paginas/registrate.html", {"form": form})

#Recuperacion de contraseña
class CustomPasswordResetView(auth_views.PasswordResetView):
    template_name = "contrasena/recuperar_contrasena.html"
    email_template_name = "contrasena/recuperar_contrasena_email.html"
    subject_template_name = "contrasena/recuperar_contrasena_asunto.txt"
    html_email_template_name = "contrasena/recuperar_contrasena_email.html"
    success_url = reverse_lazy('password_reset_done')

    def form_valid(self, form):
        # Opcional: puedes añadir lógica adicional aquí
        return super().form_valid(form)

class CustomPasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = "contrasena/recuperar_contrasena_enviado.html"

class CustomPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = "contrasena/restablecer_contrasena.html"
    success_url = reverse_lazy('password_reset_complete')

class CustomPasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = "contrasena/restablecer_contrasena_completado.html"

# URLs que usarías en tu urls.py
password_reset_views = {
    'password_reset': CustomPasswordResetView.as_view(),
    'password_reset_done': CustomPasswordResetDoneView.as_view(),
    'password_reset_confirm': CustomPasswordResetConfirmView.as_view(),
    'password_reset_complete': CustomPasswordResetCompleteView.as_view(),
}
def gestion(request):
    messages.success(request, f"¡Bienvenido, {request.user.username}!")
    return render(request, "sistema/gestion.html")
