from django.contrib import admin
from .models import Articulo, Categoria, Etiqueta

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)

@admin.register(Etiqueta)
class EtiquetaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'categoria', 'publicado', 'fecha_creacion')
    list_filter = ('publicado', 'categoria', 'fecha_creacion')
    search_fields = ('titulo', 'contenido')
    filter_horizontal = ('etiquetas',)
    autocomplete_fields = ('autor',)
