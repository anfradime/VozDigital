import os
from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractUser

# Función para generar nombre aleatorio de la imagen
def ruta_foto_perfil(instance, filename):
    ext = filename.split('.')[-1]
    nombre_archivo = f"{uuid4().hex}.{ext}"
    return os.path.join('fotos_perfil', nombre_archivo)

# Modelo personalizado de usuario
class Usuario(AbstractUser):
    TIPO_CHOICES = (
        ('administrador', 'Administrador'),
        ('lector', 'Lector'),
        ('autor', 'autor'),
        ('editor', 'Editor'),
    )

    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='lector')

    def __str__(self):
        return f"{self.username} ({self.tipo})"

# Perfil de usuario extendido
class Perfil(models.Model):
    GENERO_CHOICES = (
        ('masculino', 'Masculino'),
        ('femenino', 'Femenino'),
        ('otro', 'Otro'),
    )

    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='perfil')
    foto = models.ImageField(upload_to=ruta_foto_perfil, null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    genero = models.CharField(max_length=10, choices=GENERO_CHOICES, null=True, blank=True)
    contacto = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"Perfil de {self.usuario.username}"
