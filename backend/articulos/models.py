from django.db import models
from django.utils import timezone
from usuarios.models import Usuario

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre


class Articulo(models.Model):
    ESTADO_CHOICES = (
        ('borrador', 'Borrador'),
        ('publicado', 'Publicado'),
    )

    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    cuerpo = models.TextField()
    imagen_destacada = models.ImageField(upload_to='articulos/', blank=True, null=True)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='articulos')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    etiquetas = models.ManyToManyField(Etiqueta, blank=True)
    video_url = models.URLField(blank=True, null=True, help_text="URL de un video relacionado (YouTube, Vimeo, etc.)")
    creado = models.DateTimeField(default=timezone.now)
    actualizado = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='borrador')

    class Meta:
        ordering = ['-creado']

    def __str__(self):
        return self.titulo


class ImagenArticulo(models.Model):
    articulo = models.ForeignKey(Articulo, related_name='imagenes', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='articulos/imagenes/')
    descripcion = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Imagen para: {self.articulo.titulo}"
