
from functools import wraps
from rest_framework.response import Response
from rest_framework import status

def is_admin(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user and request.user.admin_check:
            return view_func(request, *args, **kwargs)
        else:
            return Response({'error': 'Acceso no autorizado'}, status=status.HTTP_403_FORBIDDEN)

    return _wrapped_view
