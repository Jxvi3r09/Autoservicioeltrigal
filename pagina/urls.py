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
<<<<<<< HEAD
    
    path('inicio/', views.modal_inicio, name='inicio'),
    
    path("registrate/", views.registro, name="register"), 
=======

    path("register/", views.registro, name="registro"),  # Ruta para el registro
>>>>>>> productos
    
    path("inicio/", views.inicio, name="inicio"),

    path('inventario/', views.inventario, name='inventario'),

    path('administrador/', views.administrador, name='administrador'),

<<<<<<< HEAD
    path('proveedores/', views.proveedores, name='proveedores'),
=======
    path('usuarios', views.lista_usuarios, name='usuarios'),

    path("inicioinv/", views.inicioinv, name="inicioinv"),
>>>>>>> productos


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