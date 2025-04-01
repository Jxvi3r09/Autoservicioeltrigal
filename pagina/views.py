from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import RegistroUsuarioForm  # Asegúrate de importar el formulario


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

def gestion(request):
    messages.success(request, f"¡Bienvenido, {request.user.username}!")
    return render(request, "sistema/gestion.html")
