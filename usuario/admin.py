from django.contrib import admin
from .models import AdminUser, NormalUser, faltas
from .models import NormalUser
from .forms import NormalUserForm, AdminUserForm
from django.contrib.auth.admin import UserAdmin


@admin.register(faltas)
class faltasAdmin(admin.ModelAdmin):
    pass



class NormalUserAdmin(UserAdmin):
    add_form = NormalUserForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields':('user', 'password', 'first_name', 'last_name','huella', 'is_staff'),

        }),
    )

admin.site.register(NormalUser, NormalUserAdmin)

class AdminUserAdmin(UserAdmin):
    add_form = AdminUserForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields':('user', 'password', 'is_staff'),

        }),
    )

admin.site.register(AdminUser, NormalUserAdmin)