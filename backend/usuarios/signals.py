from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Usuario, Perfil

@receiver(post_save, sender=Usuario)
def crear_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance)

@receiver(post_save, sender=Usuario)
def guardar_perfil_usuario(sender, instance, **kwargs):
    # Solo guarda si el perfil ya existe
    if hasattr(instance, 'perfil'):
        instance.perfil.save()
