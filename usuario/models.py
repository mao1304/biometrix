from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission, AbstractBaseUser,PermissionsMixin

    
class NormalUser( AbstractUser):   

    user = models.CharField(max_length=50, unique=True, primary_key=True, blank=False, default=None)
    huella = models.CharField(max_length=200)
    is_staff = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Usuario Normal'  
        verbose_name_plural = 'Usuarios Normales'  
   
    
    groups = models.ManyToManyField(Group, related_name='normaluser_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='normaluser_permissions')

    
    def __str__(self):
        return self.username

class AdminUser(AbstractUser):
    is_staff = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'Usuario administrador'  
        verbose_name_plural = 'Usuarios administradores'  

    groups = models.ManyToManyField(Group, related_name='adminuser_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='adminuser_permissions')

    def __str__(self):
        return self.username

class faltas(models.Model):
    fecha = models.DateTimeField()
    ID_profesor = models.ForeignKey(NormalUser, on_delete = models.DO_NOTHING)
    