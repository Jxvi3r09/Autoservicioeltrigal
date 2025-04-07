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



urlpatterns = [
    path('',views.principal, name='principal'),
    
    path('bienvenido', views.index, name='index'),
    
    path('inicio/', views.modal_inicio, name='inicio'),
    
    path("registrate/", views.registro, name="register"), 

    path("register/", views.registro, name="registro"),  # Ruta para el registro
    
    path("inicio/", views.inicio, name="inicio"),

    path('inventario/', views.inventario, name='inventario'),

    path('administrador/', views.lista_usuarios, name='administrador'),

    path('proveedores/', views.proveedores, name='proveedores'),

    path('usuarios', views.lista_usuarios, name='usuarios'),
    
    path('usuarios/editar/<int:id>/', views.editar_usuario, name='editar_usuario'),
    
    path('usuarios/eliminar/<int:id>/', views.eliminar_usuario, name='eliminar_usuario'),

    path("inicioinv/", views.inicioinv, name="inicioinv"),

    path('productos', views.productos, name='productos'),

    path('modal_inicio', views.modal_inicio, name='modal inicio'),


    # ✅ Nueva ruta para iniciar sesión
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),

    # ✅ Nueva ruta para cerrar sesión
    path("logout/", auth_views.LogoutView.as_view(next_page='index'), name="logout"),

    # Recuperación de contraseña 
   path('recuperar_contrasena/', CustomPasswordResetView.as_view(), name='password_reset'),
   
   path('recuperar_contrasena/enviado/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
   
   path('restablecer/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
   
   path('restablecer/completado/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),


]
# Archivos estáticos
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)