from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

    
class NewUser(AbstractUser, PermissionsMixin):

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    def __str__(self):
        return self.username
    
    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"
        verbose_name = 'Usuario'  
        verbose_name_plural = 'Usuarios'  
   
    username = models.CharField(max_length=50, unique=True, primary_key=True)
    
class faltas(models.Model):
    fecha = models.DateTimeField()
    ID_profesor = models.ForeignKey(NewUser, on_delete = models.DO_NOTHING)
    
    def __str__(self):
        return self.ID_profesor.username
    