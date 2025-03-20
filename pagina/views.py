from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

def index(request):
    return render(request, "paginas/index.html")

def inicio(request):
    return render(request, "paginas/inicio.html")

def registrate(request):
    if request.method == "POST":
        usuario = request.POST.get("usuario")
        contraseña = request.POST.get("contraseña")
        
        # Aquí puedes guardar los datos en la base de datos si es necesario

        messages.success(request, "¡Registro exitoso! Ahora puedes iniciar sesión.")  # Mensaje de éxito
        
        return redirect("inicio")  # Redirige solo si el usuario se registra correctamente
    
    return render(request, "paginas/registrate.html")  # Cargar la página de registro si no es POST

def inicio_inventario(request):
    return render(request, "sistema/inicio_inventario.html")