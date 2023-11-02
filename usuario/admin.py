from django.contrib import admin
from .models import Usuadm, Profesor

@admin.register(Usuadm)
class UsuadmAdmin(admin.ModelAdmin):
    pass

@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    pass