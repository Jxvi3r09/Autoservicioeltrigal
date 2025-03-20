#Rutas de acceso a las diferentes paginas
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from.import views

urlpatterns = [
    path('', views.index, name='index'),
    path('inicio/',views.inicio,name='inicio'),
    path('registrate/',views.registrate,name='registrate'),
    path('inicio_inventario',views.inicio_inventario, name='inventario'),
]



#Archivos estaticos
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)