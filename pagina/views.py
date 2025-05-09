from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import RegistroUsuarioForm  # Asegúrate de importar el formulario
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.views import PasswordResetView
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login
from .forms import ProductoForm
from .models import Producto
from django.utils import timezone
from datetime import timedelta
from .forms import CustomPasswordResetForm
from django.core.mail import send_mail




from .models import Usuario

#mostrar todos los usuarios
def lista_usuarios(request):
    # Obtener todos los usuarios
    usuarios = Usuario.objects.all()
    
    # Obtener el formulario
    form = RegistroUsuarioForm()
    
    # Calcular métricas estadísticas
    total_usuarios = usuarios.count()
    
    # Usuarios activos (últimos 30 días)
    usuarios_activos = usuarios.filter(
        last_login__gte=timezone.now() - timedelta(days=30)
    ).count()
    
    # Administradores (asumiendo que hay un campo 'rol' en tu modelo)
    administradores = usuarios.filter(rol='Admin').count()
    
    # Usuarios inactivos (más de 30 días sin login)
    inactivos_30dias = usuarios.filter(
        last_login__lt=timezone.now() - timedelta(days=30)
    ).count()
    
    # Porcentaje de cambio (puedes ajustar esta lógica según tus necesidades)
    # Esto es un ejemplo - deberías implementar tu propia lógica de comparación
    try:
        cambio_activos = round((usuarios_activos / total_usuarios) * 100, 1)
    except ZeroDivisionError:
        cambio_activos = 0
    
    context = {
        'usuarios': usuarios,
        'form': form,
        'total_usuarios': total_usuarios,
        'usuarios_activos': usuarios_activos,
        'administradores': administradores,
        'inactivos_30dias': inactivos_30dias,
        'cambio_activos': cambio_activos,
    }
    
    return render(request, 'sistema/administrador.html', context)

def editar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)

    if request.method == 'POST':
        usuario.tipo_documento = request.POST.get('tipo_documento')
        usuario.numero_documento = request.POST.get('numero_documento')
        usuario.first_name = request.POST.get('first_name')
        usuario.last_name = request.POST.get('last_name')
        usuario.rol = request.POST.get('rol')
        usuario.contacto = request.POST.get('contacto')
        usuario.username = request.POST.get('username')

        # Validar que ningún campo esté vacío (opcional pero recomendado)
        if all([
            usuario.tipo_documento, usuario.numero_documento,
            usuario.first_name, usuario.last_name,
            usuario.rol, usuario.contacto, usuario.username
        ]):
            usuario.save()
            messages.success(request, 'Usuario actualizado correctamente.')
        else:
            messages.error(request, 'Todos los campos son obligatorios.')

        return redirect('usuarios')  # Redirige a la vista de gestión/listado

    return redirect('usuarios')  # Previene accesos por GET no permitidos

def eliminar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)

    if request.method == 'POST':
        usuario.delete()
        return redirect('usuarios')  

    return render(request, 'sistema/administrador.html', {'usuario': usuario})
    
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

def agregar_proveedor(request):
    return render(request, "sistema/agregar_proveedor.html")

def modal_inicio(request):
    # if request.method == "POST":
    #     username = request.POST.get("username", "").strip()
    #     password = request.POST.get("password", "").strip()

    #     # Validación: campos vacíos
    #     if not username or not password:
    #         messages.error(request, "⚠️ Todos los campos son obligatorios.")
    #         return redirect("inicio")

    #     # Intentar autenticar al usuario
    #     user = authenticate(request, username=username, password=password)

    #     if user is not None:
    #         if user.is_active:
    #             login(request, user)
    #             messages.success(request, f"✅ ¡Bienvenido al sistema, {user.first_name} {user.last_name}!")
    #             return redirect("inventario")
    #         else:
    #             messages.error(request, "⚠️ Tu cuenta está inactiva. Contacta al administrador.")
    #     else:
    #         messages.error(request, "❌ Usuario o contraseña incorrectos.")

    return render(request, "paginas/principal.html")


def inicio(request):
    return render(request, "paginas/principal.html")

# def registro(request):
#     if request.method == 'POST':
#         form = RegistroUsuarioForm(request.POST)
#         if form.is_valid():
#             # Guarda el usuario pero no lo loguea automáticamente
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data['password'])  # Encripta la contraseña
#             user.save()
#             return redirect('exito')  # Redirige a una página de éxito
#     else:
#         form = RegistroUsuarioForm()
    
#     return render(request, 'paginas/registrate.html', {'form': form})
def registro(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.set_password(form.cleaned_data["password1"])
            usuario.save()
            login(request, usuario)
            return redirect("usuarios")
        else:
            return render(request, "paginas/registrate.html", {
                "form": form,
                "mostrar_modal": True
            })
    else:
        form = RegistroUsuarioForm()

    return render(request, "paginas/registrate.html", {"form": form})


# Recuperación de contraseña
class CustomPasswordResetView(auth_views.PasswordResetView):
    template_name = "contrasena/recuperar_contrasena.html"
    email_template_name = "contrasena/recuperar_contrasena_email.html"
    subject_template_name = "contrasena/recuperar_contrasena_asunto.txt"
    html_email_template_name = "contrasena/recuperar_contrasena_email.html"
    success_url = reverse_lazy('password_reset_done')
    form_class = CustomPasswordResetForm

    def form_valid(self, form):
        messages.success(self.request, "Se han enviado las instrucciones a tu correo.")
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
    return render(request, "sistema/gestion.html")

# Validacion del login
def inicioinv(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('inicioinv')  # Redirige al panel o inicio
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
            return redirect('principal')  # Reemplaza por tu URL donde está el modal login

    return render(request, "sistema/inicioinv.html")


#gestion de productos
def productos(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('productos')  # Cambia a tu URL name si es diferente
    else:
        form = ProductoForm()

    productos = Producto.objects.all()
    return render(request, 'sistema/crud_productos/productos.html', {
        'form': form,
        'productos': productos
    })
def crear_producto(request):
    form = ProductoForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('productos')
    return render(request, 'crud_productos/form_productos.html', {'form': form})

def editar_producto(request, pk):
    prod = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=prod)
        if form.is_valid():
            form.save()
            return redirect('productos')
    else:
        form = ProductoForm(instance=prod)
    return render(request, 'sistema/crud_productos/editar_producto.html', {
        'form': form,
    })

def eliminar_producto(request, pk):
    prod = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        prod.delete()
        return redirect('productos')
    return render(request, 'sistema/crud_productos/eliminar_producto.html', {
        'producto': prod,
    })


from .models import Proveedor
from .forms import ProveedorForm

def listar_proveedores(request):
    proveedores = Proveedor.objects.all().order_by('-fecha_registro')
    form = ProveedorForm()
    return render(request, 'sistema/proveedores.html', {'proveedores': proveedores, 'form': form})


def agregar_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_proveedores')  
    else:
        form = ProveedorForm()
    return render(request, 'sistema/proveedores.html', {'form': form})


def editar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)

    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('proveedores')  # Usa el nombre correcto del URL de la lista
    return redirect('proveedores')  # Evita renderizar otra plantilla


def eliminar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('listar_proveedores')
    return render(request, 'sistema/crud_proveedores/confirmar_eliminar.html', {'proveedor': proveedor})
