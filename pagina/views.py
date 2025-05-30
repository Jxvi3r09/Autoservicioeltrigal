from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, FileResponse
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login  # Agregar logout aquí
from django.utils import timezone
from datetime import timedelta  # Add this import
from django.conf import settings
import os
import subprocess
import zipfile
import shutil
from .models import Backup
from .forms import RegistroUsuarioForm  # Asegúrate de importar el formulario
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.views import PasswordResetView
from django.core.mail import send_mail
from .models import Proveedor
from .forms import ProveedorForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import ConfiguracionRespaldo
from .forms import ConfiguracionRespaldoForm
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.db import transaction
from .models import Pedido, DetallePedido, Venta, DetalleVenta
from decimal import Decimal
import json

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
        usuario.contacto = request.POST.get('email')
        usuario.username = request.POST.get('username')

        # Validar que ningún campo esté vacío (opcional pero recomendado)
        if all([
            usuario.tipo_documento, usuario.numero_documento,
            usuario.first_name, usuario.last_name,
            usuario.rol, usuario.email, usuario.username
        ]):
            usuario.save()
            messages.success(request, 'Usuario actualizado correctamente.')
        else:
            messages.error(request, 'Todos los campos son obligatorios.')

        return redirect('usuarios')  # Redirige a la vista de gestión/listado

    return redirect('usuarios')  # Previene accesos por GET no permitidos

def eliminar_usuario(request, id):
    messages.success(request, "¡Usuario eliminado exitosamente!")
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
    productos = Producto.objects.all().select_related('categoria')
    categorias = Categoria.objects.all()
    return render(request, 'sistema/inventario.html', {
        'productos': productos,
        'categorias': categorias,
    })

def agregar_categoria(request):
    if request.method == 'POST':
        try:
            nombre = request.POST.get('nombre')
            categoria = Categoria.objects.create(nombre=nombre)
            return JsonResponse({
                'success': True,
                'categoria': {
                    'id': categoria.id,
                    'nombre': categoria.nombre
                }
            })
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Método no permitido'})

def administrador(request):
    return render(request, "sistema/administrador.html")

def proveedores(request):
    return render(request, "sistema/proveedores.html")

def agregar_proveedor(request):
    return render(request, "sistema/agregar_proveedor.html")

def modal_inicio(request):
    return render(request, "paginas/modal_inicio.html")


# def inicio(request):
#     return render(request, "paginas/principal.html")

# # def registro(request):
# #     if request.method == 'POST':
# #         form = RegistroUsuarioForm(request.POST)
# #         if form.is_valid():
# #             # Guarda el usuario pero no lo loguea automáticamente
# #             user = form.save(commit=False)
# #             user.set_password(form.cleaned_data['password'])  # Encripta la contraseña
# #             user.save()
# #             return redirect('exito')  # Redirige a una página de éxito
# #     else:
# #         form = RegistroUsuarioForm()
    
# #     return render(request, 'paginas/registrate.html', {'form': form})
def registro(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.set_password(form.cleaned_data["password1"])
            usuario.save()
            messages.success(request, "¡Usuario registrado exitosamente!")
            # login(request, usuario)
            return redirect("usuarios")
        else:
            # Al pasar el formulario con errores, mostramos el modal
            return render(request, "paginas/registrate.html", {
                "form": form,
                "mostrar_modal": True  # Esto muestra el modal si hay errores
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
    # form_class = CustomPasswordResetForm

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
    context = {
        'total_productos': Producto.objects.count(),
        'total_proveedores': Proveedor.objects.count(),
        'total_usuarios': Usuario.objects.count(),
        'stock_bajo': Producto.objects.filter(cantidad_producto__lte=10).count(),
    }
    return render(request, "sistema/inicioinv.html", context)

#gestion de productos
def productos(request):
    categorias = Categoria.objects.all()  # Obtén las categorías
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('productos')
    else:
        form = ProductoForm()

    productos = Producto.objects.all()
    return render(request, 'sistema/crud_productos/productos.html', {
        'form': form,
        'productos': productos,
        'categorias': categorias  # Pasa las categorías al template
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

def obtener_producto(request, pk):
    try:
        producto = Producto.objects.get(id=pk)
        return JsonResponse({
            'id': producto.id,
            'nombre': producto.nombre,
            'categoria': producto.categoria.id,
            'precio': float(producto.precio),
            'cantidad': producto.cantidad
        })
    except Producto.DoesNotExist:
        return JsonResponse({'error': 'Producto no encontrado'}, status=404)

def editar_producto(request, pk):
    if request.method == 'POST':
        try:
            producto = Producto.objects.get(id=pk)
            producto.nombre = request.POST['nombre']
            producto.categoria_id = request.POST['categoria']
            producto.precio = request.POST['precio']
            producto.cantidad = request.POST['cantidad']
            
            if 'imagen' in request.FILES:
                producto.imagen = request.FILES['imagen']
            
            producto.save()
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Método no permitido'})

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


@login_required
def perfil_usuario(request):
    usuario = request.user
    context = {
        'usuario': usuario,
    }
    return render(request, 'sistema/perfil_usuario.html', context)


@login_required
def actualizar_imagen_perfil(request):
    if request.method == 'POST' and request.FILES.get('imagen_perfil'):
        request.user.imagen_perfil = request.FILES['imagen_perfil']
        request.user.save()
    return redirect('perfil_usuario')


def editar_foto_usuario(request):
    usuario = request.user

    if request.method == 'POST':
        accion = request.POST.get('accion')

        if accion == 'eliminar' and usuario.imagen_perfil:
            usuario.imagen_perfil.delete()
            usuario.imagen_perfil = None
            usuario.save()
            # Puedes usar mensajes para confirmar al usuario
        elif accion == 'cambiar' and 'imagen_perfil' in request.FILES:
            usuario.imagen_perfil = request.FILES['imagen_perfil']
            usuario.save()

    return redirect('perfil_usuario')


from .models import Categoria, Producto
from .forms import CategoriaForm



from .forms import CategoriaForm


def listar_categorias(request):
    categorias = Categoria.objects.all()
    form = CategoriaForm()
    return render(request, 'sistema/inventario.html', {
        'categorias': categorias,
        'form': form,
    })

def registrar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('listar_categorias')  


def categoria_detalle(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    productos = Producto.objects.filter(categoria=categoria)
    return render(request, 'sistema/inventario/categoria_detalle.html', {
        'categoria': categoria,
        'productos': productos,
    })


from django.shortcuts import render, get_object_or_404, redirect
from .models import Categoria

def categoria_editar(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)

    if request.method == 'POST':
        nuevo_nombre = request.POST.get('nombre')
        if nuevo_nombre:
            categoria.nombre = nuevo_nombre
            categoria.save()
        return redirect('inventario')

    return redirect('inventario')

def categoria_eliminar(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)

    if request.method == 'POST':
        categoria.delete()
        messages.success(request, 'Categoría eliminada correctamente.')
        return redirect('inventario')  # Asegúrate de tener esta URL definida

    return render(request, 'sistema/inventario/categoria_confirmar_eliminar.html', {
        'categoria': categoria
    })

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Categoria

def editar_categoria(request, categoria_id):
    if request.method == 'POST':
        try:
            categoria = get_object_or_404(Categoria, id=categoria_id)
            categoria.nombre = request.POST['nombre']
            categoria.descripcion = request.POST.get('descripcion', '')
            categoria.save()
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Método no permitido'})

def eliminar_categoria(request, categoria_id):
    if request.method == 'DELETE':
        try:
            categoria = get_object_or_404(Categoria, id=categoria_id)
            categoria.delete()
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Método no permitido'})

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Categoria

def modal_registro_categoria(request):
    return render(request, 'sistema/modal_registro_categoria.html')

def guardar_categoria(request):
    if request.method == 'POST':
        try:
            categoria = Categoria.objects.create(
                nombre=request.POST['nombre'],
                descripcion=request.POST.get('descripcion', '')
            )
            messages.success(request, 'Categoría guardada correctamente')
            return redirect('inventario')
        except Exception as e:
            messages.error(request, f'Error al guardar la categoría: {str(e)}')
            return redirect('modal_registro_categoria')
    return redirect('modal_registro_categoria')

from django.http import JsonResponse
from .models import Producto

# def agregar_producto(request):
#     if request.method == 'POST':
#         try:
#             producto = Producto.objects.create(
#                 nombre=request.POST['nombre'],
#                 categoria_id=request.POST['categoria'],
#                 precio=request.POST['precio']
#             )
#             if 'imagen' in request.FILES:
#                 producto.imagen = request.FILES['imagen']
#                 producto.save()
#             return JsonResponse({'success': True})
#         except Exception as e:
#             return JsonResponse({'success': False, 'error': str(e)})
#     return JsonResponse({'success': False, 'error': 'Método no permitido'})

from django.http import JsonResponse
from .models import Producto

def eliminar_producto(request, id):
    if request.method == 'POST':
        try:
            producto = Producto.objects.get(id=id)
            producto.delete()
            return JsonResponse({'success': True})
        except Producto.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Producto no encontrado'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Método no permitido'})

# COPIAS DE SEGURIDAD 
class CopiasBDView(LoginRequiredMixin, View):
    """Vista para el panel de respaldos"""
    def get(self, request):
        context = {
            'title': 'Gestión de Respaldos',
            'backups': []  # Aquí puedes agregar backups existentes si los tienes
        }
        return render(request, 'sistema/copiasbd.html', context)
    
    
class GenerarBackupView(LoginRequiredMixin, View):
    """Vista para generar y descargar el backup"""
    def post(self, request):
        # Nombre del archivo con fecha/hora
        filename = f"backup_{timezone.now().strftime('%Y-%m-%d_%H-%M-%S')}.sql"
        filepath = os.path.join(settings.BASE_DIR, 'respaldos', filename)

        # Crear carpeta de respaldos si no existe
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        # Datos de conexión (ajusta según tu configuración)
        db_name = settings.DATABASES['default']['NAME']
        db_user = settings.DATABASES['default']['USER']
        db_password = settings.DATABASES['default']['PASSWORD']
        db_host = settings.DATABASES['default']['HOST'] or 'localhost'
        db_port = settings.DATABASES['default']['PORT'] or '3306'

        # Comando para realizar el backup (MySQL)
        command = f"mysqldump -u {db_user} -p{db_password} -h {db_host} -P {db_port} {db_name} > {filepath}"

        # Ejecutar el comando
        result = subprocess.run(command, shell=True)

        if result.returncode == 0 and os.path.exists(filepath):
            # Devolver el archivo como descarga
            return FileResponse(open(filepath, 'rb'), as_attachment=True, filename=filename)
        else:
            return HttpResponse("Error al generar el respaldo.", status=500)
        
# COPIAS DE SEGURIDAD AUTOMATICA def configurar_respaldo(request):
def configurar_respaldo(request):
    print("¡La vista configurar_respaldo fue llamada!")  # Este mensaje debe aparecer en la consola

    # Obtener la configuración de respaldo, o crearla si no existe
    config, created = ConfiguracionRespaldo.objects.get_or_create(id=1)
    print(f"Configuración cargada: {config}")  # Verifica que la configuración se cargue correctamente

    if request.method == 'POST':
        form = ConfiguracionRespaldoForm(request.POST, instance=config)
        if form.is_valid():
            form.save()
            print("Formulario guardado correctamente")  # Mensaje cuando el formulario se guarda
            return redirect('configurar_respaldo')
    else:
        form = ConfiguracionRespaldoForm(instance=config)

    # Verifica si el formulario tiene campos
    print("Campos del formulario:", form.fields)  # Esto debería mostrar los campos del formulario

    return render(request, 'sistema/copiasbd.html', {'form': form, 'config': config})

from .forms import RespaldoForm  # Agregar este import al inicio del archivo
from .models import Backup

def generar_backup(request):
    try:
        # Crear carpeta de respaldos si no existe
        backup_dir = os.path.join(settings.BASE_DIR, 'respaldos')
        os.makedirs(backup_dir, exist_ok=True)

        # Generar nombres de archivos con timestamp
        timestamp = timezone.now().strftime('%Y%m%d_%H%M%S')
        sql_filename = f"backup_{timestamp}.sql"
        media_filename = f"backup_{timestamp}_media.zip"
        
        sql_filepath = os.path.join(backup_dir, sql_filename)
        media_filepath = os.path.join(backup_dir, media_filename)

        # 1. Respaldo de base de datos
        db = settings.DATABASES['default']
        command = [
            'mysqldump',
            f'-u{db["USER"]}',
            f'-p{db["PASSWORD"]}',
            f'-h{db.get("HOST", "localhost")}',
            f'-P{db.get("PORT", "3306")}',
            db['NAME'],
            f'--result-file={sql_filepath}'
        ]
        subprocess.run(command, check=True)

        # 2. Respaldo de archivos multimedia
        media_dir = os.path.join(settings.BASE_DIR, 'media')
        if os.path.exists(media_dir):
            with zipfile.ZipFile(media_filepath, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, _, files in os.walk(media_dir):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arc_name = os.path.relpath(file_path, settings.BASE_DIR)
                        zipf.write(file_path, arc_name)

        # Calcular tamaño total
        total_size = os.path.getsize(sql_filepath)
        if os.path.exists(media_filepath):
            total_size += os.path.getsize(media_filepath)

        # Crear registro en la base de datos
        Backup.objects.create(
            fecha=timezone.now(),
            tipo='Manual',
            tamano=f"{total_size / (1024 * 1024):.2f} MB",
            estado='Completado',
            archivo=sql_filename
        )

        messages.success(request, "Respaldo generado correctamente")
        print(f"Respaldo guardado en: {sql_filepath}")
        if os.path.exists(media_filepath):
            print(f"Archivos multimedia guardados en: {media_filepath}")

    except Exception as e:
        messages.error(request, f"Error al generar respaldo: {str(e)}")
        print(f"Error detallado: {str(e)}")

    return redirect('copias_bd')

def copias_bd(request):
    if request.method == 'POST':
        form = RespaldoForm(request.POST)
        if form.is_valid():
            # Guardar configuración
            messages.success(request, 'Configuración guardada correctamente')
            return redirect('copias_bd')
    else:
        form = RespaldoForm()

    backups = Backup.objects.all().order_by('-fecha')
    
    context = {
        'form': form,
        'backups': backups,
        'estadisticas': {
            'total_backups': backups.count(),
            'espacio_usado': get_backups_size(),
            'ultimo_auto': get_last_auto_backup(),
            'config_actual': get_current_config()
        }
    }
    return render(request, 'sistema/copiasbd.html', context)

def descargar_backup(request, id):
    backup = get_object_or_404(Backup, id=id)
    filepath = os.path.join(settings.BASE_DIR, 'respaldos', backup.archivo)
    if os.path.exists(filepath):
        return FileResponse(open(filepath, 'rb'), as_attachment=True, filename=backup.archivo)
    messages.error(request, "Archivo de respaldo no encontrado")
    return redirect('copias_bd')

def eliminar_backup(request, id):
    backup = get_object_or_404(Backup, id=id)
    try:
        # Eliminar archivo físico
        filepath = os.path.join(settings.BASE_DIR, 'respaldos', backup.archivo)
        if os.path.exists(filepath):
            os.remove(filepath)
        backup.delete()
        messages.success(request, "Respaldo eliminado correctamente")
    except Exception as e:
        messages.error(request, f"Error al eliminar el respaldo: {str(e)}")
    return redirect('copias_bd')

def restaurar_backup(request, id):
    backup = get_object_or_404(Backup, id=id)
    try:
        # 1. Restaurar base de datos
        sql_filepath = os.path.join(settings.BASE_DIR, 'respaldos', backup.archivo)
        media_backup = sql_filepath.replace('.sql', '_media.zip')

        if not os.path.exists(sql_filepath):
            raise FileNotFoundError("Archivo de respaldo SQL no encontrado")

        # Restaurar SQL
        db_settings = settings.DATABASES['default']
        command = f"mysql -u {db_settings['USER']} {db_settings['NAME']} < {sql_filepath}"
        subprocess.run(command, shell=True, check=True)

        # 2. Restaurar imágenes de perfil
        media_dir = os.path.join(settings.BASE_DIR, 'media')
        if os.path.exists(media_backup):
            # Limpiar directorio media actual
            if os.path.exists(media_dir):
                shutil.rmtree(media_dir)
            os.makedirs(media_dir, exist_ok=True)

            # Extraer archivos multimedia
            with zipfile.ZipFile(media_backup, 'r') as zip_ref:
                zip_ref.extractall(settings.BASE_DIR)

            messages.success(request, "Respaldo y archivos multimedia restaurados correctamente")
        else:
            messages.warning(request, "SQL restaurado, pero no se encontró respaldo de archivos multimedia")

    except Exception as e:
        messages.error(request, f"Error durante la restauración: {str(e)}")
        print(f"Error detallado: {str(e)}")  # Para debugging
    
    return redirect('copias_bd')

import os
from django.conf import settings
from django.utils import timezone

def get_backups_size():
    total_size = 0
    backup_dir = os.path.join(settings.BASE_DIR, 'respaldos')
    
    if os.path.exists(backup_dir):
        for file in os.listdir(backup_dir):
            file_path = os.path.join(backup_dir, file)
            if os.path.isfile(file_path):
                total_size += os.path.getsize(file_path)
    
    return f"{total_size / (1024 * 1024):.2f} MB"

def get_last_auto_backup():
    ultimo_backup = Backup.objects.filter(tipo='Automático').order_by('-fecha').first()
    return ultimo_backup.fecha.strftime('%d/%m/%Y') if ultimo_backup else 'No hay'

def get_current_config():
    config = ConfiguracionRespaldo.objects.first()
    return f"{config.frecuencia} - {config.hora}" if config else "No configurado"

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Producto

@csrf_exempt
def guardar_producto(request):
    if request.method == 'POST':
        try:
            producto = Producto(
                id=request.POST.get('id'),
                nombre=request.POST.get('nombre'),
                categoria_id=request.POST.get('categoria'),
                precio=request.POST.get('precio'),
                cantidad_producto=request.POST.get('cantidad_producto')
            )
            
            if 'imagen' in request.FILES:
                producto.imagen = request.FILES['imagen']
                
            producto.save()
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Método no permitido'})

def obtener_producto(request, id):
    try:
        producto = get_object_or_404(Producto, id=id)
        data = {
            'id': producto.id,
            'nombre': producto.nombre,
            'categoria': producto.categoria.id,
            'precio': str(producto.precio),
            'cantidad_producto': producto.cantidad_producto,
            'imagen': producto.imagen.url if producto.imagen else None
        }
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

def editar_producto(request, id):
    if request.method == 'POST':
        producto = get_object_or_404(Producto, id=id)
        form_data = {
            'nombre': request.POST.get('nombre'),
            'categoria': request.POST.get('categoria'),
            'precio': request.POST.get('precio'),
            'cantidad_producto': request.POST.get('cantidad_producto'),
        }
        if 'imagen' in request.FILES:
            form_data['imagen'] = request.FILES['imagen']
            
        form = ProductoForm(form_data, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False, 'error': 'Método no permitido'})

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Producto

def obtener_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    data = {
        'id': producto.id,
        'nombre': producto.nombre,
        'categoria': producto.categoria_id,
        'precio': str(producto.precio),
        'cantidad_producto': producto.cantidad_producto
    }
    return JsonResponse(data)

def editar_producto(request, id):
    if request.method == 'POST':
        try:
            producto = get_object_or_404(Producto, id=id)
            producto.nombre = request.POST.get('nombre')
            producto.categoria_id = request.POST.get('categoria')
            producto.precio = request.POST.get('precio')
            producto.cantidad_producto = request.POST.get('cantidad_producto')
            
            if 'imagen' in request.FILES:
                producto.imagen = request.FILES['imagen']
            
            producto.save()
            return JsonResponse({'success': True})
        except Exception as e:
            print('Error:', str(e))  # Para debug
            return JsonResponse({'success': False, 'error': str(e)})
    
    return JsonResponse({'success': False, 'error': 'Método no permitido'})

def pedidos(request):
    if request.method == 'POST':
        try:
            # Obtener los datos del formulario
            proveedor_id = request.POST.get('proveedor')
            fecha_entrega = request.POST.get('fecha_entrega')
            productos = request.POST.getlist('producto[]')
            cantidades = request.POST.getlist('cantidad[]')
            
            if not all([proveedor_id, fecha_entrega, productos, cantidades]):
                raise ValueError("Todos los campos son requeridos")
            
            # Crear el pedido
            pedido = Pedido.objects.create(
                proveedor_id=proveedor_id,
                fecha_entrega=fecha_entrega,
                estado='pendiente'
            )
            
            # Crear los detalles del pedido y actualizar stock
            for producto_id, cantidad in zip(productos, cantidades):
                if producto_id and cantidad:
                    cantidad = int(cantidad)
                    DetallePedido.objects.create(
                        pedido=pedido,
                        producto_id=producto_id,
                        cantidad=cantidad
                    )
                    # Actualizar stock del producto
                    Producto.objects.filter(id=producto_id).update(
                        cantidad_producto=F('cantidad_producto') + cantidad
                    )
            
            messages.success(request, 'Pedido creado exitosamente')
            return redirect('pedidos')
        
        except Exception as e:
            messages.error(request, f'Error al crear el pedido: {str(e)}')
    
    # Obtener datos para mostrar
    pedidos = Pedido.objects.all().order_by('-fecha_pedido')
    proveedores = Proveedor.objects.all()
    productos = Producto.objects.all()
    
    return render(request, 'sistema/pedidos.html', {
        'pedidos': pedidos,
        'proveedores': proveedores,
        'productos': productos,
    })

def detalle_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    return render(request, 'sistema/detalle_pedido.html', {
        'pedido': pedido
    })

def buscar_producto(request, codigo):
    try:
        producto = Producto.objects.get(id=codigo)
        return JsonResponse({
            'found': True,
            'id': producto.id,
            'nombre': producto.nombre,
            'precio': float(producto.precio),
            'stock': producto.cantidad_producto
        })
    except Producto.DoesNotExist:
        return JsonResponse({'found': False})

@login_required
def ventas(request):
    ventas_list = Venta.objects.all().order_by('-fecha_venta')
    productos = Producto.objects.all()
    return render(request, 'sistema/ventas.html', {
        'ventas': ventas_list,
        'productos': productos,
    })

@login_required
def detalle_venta(request, venta_id):
    venta = get_object_or_404(Venta.objects.prefetch_related('detalles__producto'), id=venta_id)
    return render(request, 'sistema/detalle_venta.html', {
        'venta': venta
    })

@login_required
def eliminar_venta(request, venta_id):
    venta = get_object_or_404(Venta, id=venta_id)
    if request.method == 'POST':
        venta.delete()
        messages.success(request, 'Venta eliminada correctamente')
        return redirect('ventas')
    return redirect('ventas')

@login_required
@transaction.atomic
def registrar_venta(request):
    if request.method == 'POST':
        try:
            # Obtener y validar datos
            productos_json = request.POST.get('productos_json')
            if not productos_json:
                raise ValueError('No se recibieron productos')
            
            productos_data = json.loads(productos_json)
            total = Decimal(request.POST.get('total', '0'))
            
            # Crear la venta
            venta = Venta.objects.create(
                vendedor=request.user,
                total=total,
                fecha_venta=timezone.now()
            )
            
            # Procesar cada producto
            for item in productos_data:
                producto = Producto.objects.select_for_update().get(id=item['id'])
                cantidad = int(item['cantidad'])
                precio = Decimal(str(item['precio']))
                subtotal = Decimal(str(item['subtotal']))
                
                if producto.cantidad_producto < cantidad:
                    raise ValueError(f'Stock insuficiente para {producto.nombre}')
                
                # Crear detalle de venta
                DetalleVenta.objects.create(
                    venta=venta,
                    producto=producto,
                    cantidad_vendida=cantidad,
                    precio_unitario=precio,
                    subtotal=subtotal
                )
                
                # Actualizar stock
                producto.cantidad_producto -= cantidad
                producto.save()
            
            messages.success(request, 'Venta registrada exitosamente')
            print(f"Venta {venta.id} registrada con éxito")  # Debug log
            
            return redirect('ventas')
            
        except Exception as e:
            print(f"Error al registrar venta: {str(e)}")  # Debug log
            messages.error(request, f'Error al registrar la venta: {str(e)}')
            return redirect('ventas')
    
    return redirect('ventas')




