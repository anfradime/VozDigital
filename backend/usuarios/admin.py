from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html

from .models import Usuario, Perfil

class PerfilInline(admin.StackedInline):
    model = Perfil
    can_delete = False
    verbose_name_plural = 'Perfil'
    fk_name = 'usuario'

class UsuarioAdmin(UserAdmin):
    inlines = (PerfilInline,)

    fieldsets = UserAdmin.fieldsets + (
        ('Información adicional', {'fields': ('tipo',)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Información adicional', {'fields': ('tipo',)}),
    )

    list_display = ('username', 'email', 'tipo', 'is_staff', 'mostrar_foto_perfil')

    def mostrar_foto_perfil(self, obj):
        if hasattr(obj, 'perfil') and obj.perfil.foto:
            return format_html(
                '<img src="{}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 50%;" />',
                obj.perfil.foto.url
            )
        return "Sin foto"

    mostrar_foto_perfil.short_description = 'Foto de perfil'

admin.site.register(Usuario, UsuarioAdmin)
