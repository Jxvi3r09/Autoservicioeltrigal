from django.shortcuts import render

# Create your views here.
import os
import datetime
from django.http import HttpResponse
from django.conf import settings

def generar_backup(request):
    fecha = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    nombre_archivo = f"backup_{fecha}.sql"
    ruta_archivo = os.path.join(settings.BASE_DIR, nombre_archivo)

    mysql_conf = settings.MYSQL_BACKUP
    usuario = mysql_conf['USER']
    contrasena = mysql_conf['PASSWORD']
    base_datos = mysql_conf['NAME']

    # Si no hay contraseña, omitimos el parámetro -p
    if contrasena:
        comando = f'mysqldump -u {usuario} -p{contrasena} {base_datos} > "{ruta_archivo}"'
    else:
        comando = f'mysqldump -u {usuario} {base_datos} > "{ruta_archivo}"'

    resultado = os.system(comando)

    if resultado != 0:
        return HttpResponse("❌ Error al generar la copia de seguridad. Verifica los datos y si mysqldump está disponible.")

    with open(ruta_archivo, 'rb') as archivo:
        response = HttpResponse(archivo.read(), content_type='application/sql')
        response['Content-Disposition'] = f'attachment; filename="{nombre_archivo}"'
        return response
