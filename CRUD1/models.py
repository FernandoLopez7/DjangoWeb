from django.db import models

# Create your models here.

# Esto era para el CRUD de los usuairos
class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nombre_usuario = models.CharField(max_length=50, verbose_name="Nombre del Usuario")
    email = models.EmailField(verbose_name="Correo electronico")
    tfno = models.CharField(max_length=10, verbose_name="Telefono")
    
    
# El mini core
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre
    
class Contrato(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Cliente")
    descripcion = models.CharField(max_length=100, verbose_name="Descripcion")
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    fecha_creacion = models.DateField(auto_now_add=True, verbose_name="Fecha de creacion", editable=False)
    fecha_edicion = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")