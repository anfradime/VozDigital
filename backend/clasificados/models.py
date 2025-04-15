from django.db import models
from django.conf import settings

class CategoriaClasificado(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Clasificado(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(CategoriaClasificado, on_delete=models.CASCADE)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    disponible = models.BooleanField(default=True)
    ubicacion = models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return self.titulo

class ImagenClasificado(models.Model):
    clasificado = models.ForeignKey(Clasificado, on_delete=models.CASCADE, related_name='imagenes')
    imagen = models.ImageField(upload_to='imagenes_clasificados/')

class ReporteClasificado(models.Model):
    clasificado = models.ForeignKey(Clasificado, on_delete=models.CASCADE)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    motivo = models.TextField()
    fecha_reporte = models.DateTimeField(auto_now_add=True)

class CalificacionVendedor(models.Model):
    vendedor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='calificaciones_recibidas')
    comprador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='calificaciones_realizadas')
    clasificado = models.ForeignKey(Clasificado, on_delete=models.CASCADE)
    calificacion = models.PositiveSmallIntegerField()
    comentario = models.TextField(blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
