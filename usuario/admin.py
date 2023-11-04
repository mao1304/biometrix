from django.contrib import admin
from .models import Usuadm, Profesor, faltas

@admin.register(Usuadm)
class UsuadmAdmin(admin.ModelAdmin):
    pass

@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    pass

@admin.register(faltas)
class faltasAdmin(admin.ModelAdmin):
    pass

