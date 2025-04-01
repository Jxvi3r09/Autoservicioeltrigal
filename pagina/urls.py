# Rutas de acceso a las diferentes páginas
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views  # Importamos las vistas de nuestra app

urlpatterns = [
    path('',views.principal, name='principal'),
    
    path('bienvenido', views.index, name='index'),
    
    path('inicio/', views.modal_inicio, name='inicio'),
    
    path("register/", views.registro, name="register"), 
    
    path("register/", views.registro, name="registro"),  # Ruta para el registro
    
    path('inventario/', views.inventario, name='inventario'),
    
    path('administrador/', views.administrador, name='administrador'),

    path('proveedores/', views.proveedores, name='proveedores'),

    path('agregar_proveedores/', views.agregar_proveedores, name='agregar_proveedores'),

    # ✅ Nueva ruta para iniciar sesión
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),

    # ✅ Nueva ruta para cerrar sesión
    path("logout/", auth_views.LogoutView.as_view(next_page='index'), name="logout"),

    # ✅ Nueva ruta para restablecer contraseña
    path("password_reset/", auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html"), name="password_reset"),
]

# Archivos estáticos
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
