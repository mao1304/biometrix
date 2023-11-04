from django import forms
from .models import NormalUser, AdminUser

class NormalUserForm(forms.ModelForm):
    class Meta:
        model = NormalUser
        fields = {'user', 'password', 'first_name', 'last_name','huella', 'is_staff',}

class AdminUserForm(forms.ModelForm):
    class Meta:
        model = AdminUser
        fields = {'username', 'password', 'is_staff',}  