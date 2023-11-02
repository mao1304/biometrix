from django.db import models

class Usuadm(models.Model):
    usuario = models.CharField(max_length=45)
    password = models.CharField(max_length=45)

    def __str__(self):
        return self.usuario
     
class Profesor(models.Model):
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=48)
    cedula = models.IntegerField()
    correo = models.CharField(max_length=45)
    usuario = models.CharField(max_length=45, primary_key=True)
    contraseña = models.CharField(max_length=45)
    huella = models.CharField(max_length=200)

    def __str__(self):
        return self.usuario