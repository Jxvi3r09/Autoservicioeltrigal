from django.urls import path
from .views import generar_backup

urlpatterns = [
    path('descargar/', generar_backup, name='generar_backup'),
]
