# Rutas de acceso a las diferentes páginas
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views  # Importamos las vistas de nuestra app
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import CustomPasswordResetView
from .views import CustomPasswordResetDoneView
from .views import CustomPasswordResetConfirmView
from .views import CustomPasswordResetCompleteView
from django.contrib import admin
from django.urls import path, include
from .views import CopiasBDView, GenerarBackupView
from .views import configurar_respaldo



urlpatterns = [
    path('',views.principal, name='principal'),
    
    # path('bienvenido', views.index, name='index'),
    
    path('inicio/', views.modal_inicio, name='inicio'),
    
    path("registrate/", views.registro, name="register"), 

    # path("register/", views.registro, name="registro"),  # Ruta para el registro
    
    # path("inicio/", views.inicio, name="inicio"),

    path('inventario/', views.inventario, name='inventario'),

    path('administrador/', views.lista_usuarios, name='administrador'),

    path('proveedores/', views.listar_proveedores, name='proveedores'),

    path('usuarios/', views.lista_usuarios, name='usuarios'),
    
    path('usuarios/editar/<int:id>/', views.editar_usuario, name='editar_usuario'),

    # Inabilitar usuario
    path('deshabilitar_usuario/<int:id>/', views.deshabilitar_usuario, name='deshabilitar_usuario'),
    
    # Desabilitar usuario
    path('usuarios_inhabilitados/', views.usuarios_inhabilitados, name='usuarios_inhabilitados'),
    
    # Habilitar usuario
    path('habilitar_usuario/<int:id>/', views.habilitar_usuario, name='habilitar_usuario'),
    
    path('usuarios/eliminar/<int:id>/', views.eliminar_usuario, name='eliminar_usuario'),

    path("inicioinv/", views.inicioinv, name="inicioinv"),

    path('productos', views.productos, name='productos'),

    path('modal_inicio', views.modal_inicio, name='modal inicio'),

    path('proveedores/', views.listar_proveedores, name='listar_proveedores'),
    path('agregar-proveedor/', views.agregar_proveedor, name='agregar_proveedor'),

    # ✅ Nueva ruta para iniciar sesión
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),

    # ✅ Nueva ruta para cerrar sesión
    path("logout/", auth_views.LogoutView.as_view(next_page='index'), name="logout"),



    # Recuperación de contraseña 
    path('recuperar_contrasena/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('recuperar_contrasena/enviado/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('restablecer/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('restablecer/completado/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    

    path('productos/', views.productos, name='productos'),
    path('productos/crear/', views.crear_producto, name='crear_producto'),  # NUEVA
    path('productos/obtener/<int:id>/', views.obtener_producto, name='obtener_producto'),
    path('productos/editar/<int:id>/', views.editar_producto, name='editar_producto'),
    path('productos/eliminar/<int:id>/', views.eliminar_producto, name='eliminar_producto'),
    # path('agregar-producto/', views.agregar_producto, name='agregar_producto'),

    path('proveedores/eliminar/<int:id>/', views.eliminar_proveedor, name='eliminar_proveedor'),
    path('proveedores/editar/<int:id>/', views.editar_proveedor, name='editar_proveedor'),

    path('perfil', views.perfil_usuario, name='perfil_usuario'),
    path('actualizar-imagen/', views.actualizar_imagen_perfil, name='actualizar_imagen_perfil'),

    path('perfil/editar-foto/', views.editar_foto_usuario, name='editar_foto_usuario'),

    # path('categorias/', views.listar_categorias, name='listar_categorias'),
    # path('categorias/registrar/', views.registrar_categoria, name='registrar_categoria'),

    path('categorias/<int:categoria_id>/editar/', views.categoria_editar, name='categoria_editar'),
    path('categorias/<int:categoria_id>/eliminar/', views.categoria_eliminar, name='categoria_eliminar'),

    path('categoria/<int:categoria_id>/', views.categoria_detalle, name='categoria_detalle'),
    
    # COPIAS DE SEGURIDAD BD
    path('respaldos/', CopiasBDView.as_view(), name='copias_bd'),
    path('copias-bd/', views.copias_bd, name='copias_bd'),

    path('admin/', admin.site.urls),
    
    path('backup/', include('backup.urls')),  # 👈 ¡IMPORTANTE!
    
    path('respaldos/', views.configurar_respaldo, name='configurar_respaldo'),

    path('generar-backup/', views.generar_backup, name='generar_backup'),
    path('backup/descargar/<int:id>/', views.descargar_backup, name='descargar_backup'),
    path('backup/eliminar/<int:id>/', views.eliminar_backup, name='eliminar_backup'),
    path('backup/restaurar/<int:id>/', views.restaurar_backup, name='restaurar_backup'),

    # path('categoria/<int:categoria_id>/', views.categoria_detalle, name='categoria_detalle'),

    path('agregar-categoria/', views.agregar_categoria, name='agregar_categoria'),
    path('editar-categoria/<int:categoria_id>/', views.editar_categoria, name='editar_categoria'),
    path('eliminar-categoria/<int:categoria_id>/', views.eliminar_categoria, name='eliminar_categoria'),
    
    path('editar-producto/<int:id>/', views.obtener_producto, name='obtener_producto'),
    path('productos/editar/<int:id>/', views.editar_producto, name='editar_producto'),

    path('pedidos/', views.pedidos, name='pedidos'),
    path('pedidos/detalle/<int:pedido_id>/', views.detalle_pedido, name='detalle_pedido'),

    # URLs para el módulo de ventas
    path('ventas/', views.ventas, name='ventas'),
    path('ventas/registrar/', views.registrar_venta, name='registrar_venta'),  # Add this line
    path('ventas/detalle/<int:venta_id>/', views.detalle_venta, name='detalle_venta'),
    path('ventas/eliminar/<int:venta_id>/', views.eliminar_venta, name='eliminar_venta'),
    path('buscar-producto/<str:codigo>/', views.buscar_producto, name='buscar_producto'),

    path('guardar_producto/', views.guardar_producto, name='guardar_producto'),

    path('eliminar_producto/<str:id>/', views.eliminar_producto, name='eliminar_producto'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Archivos estáticos
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)