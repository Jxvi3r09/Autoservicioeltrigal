from django.shortcuts import redirect
from django.contrib import messages
from functools import wraps

def admin_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.rol == 'administrador':
            return view_func(request, *args, **kwargs)
        messages.error(request, 'No tienes permisos para acceder a esta sección.')
        return redirect('inicioinv')
    return _wrapped_view

def empleado_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and (request.user.rol == 'empleado' or request.user.rol == 'administrador'):
            return view_func(request, *args, **kwargs)
        messages.error(request, 'No tienes permisos para acceder a esta sección.')
        return redirect('inicioinv')
    return _wrapped_view
