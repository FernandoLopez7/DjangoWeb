from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nombre_usuario = models.CharField(max_length=50, verbose_name="Nombre del Usuario")
    email = models.EmailField(verbose_name="Correo electronico")
    tfno = models.CharField(max_length=10, verbose_name="Telefono")
    