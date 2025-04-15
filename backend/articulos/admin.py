from django.contrib import admin
from .models import Articulo, Categoria, Etiqueta, ImagenArticulo

class ImagenArticuloInline(admin.TabularInline):
    model = ImagenArticulo
    extra = 1  # Cuántas líneas vacías se muestran por defecto

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
    list_display = ('titulo', 'autor', 'categoria', 'estado', 'creado')
    list_filter = ('estado', 'categoria', 'creado')
    search_fields = ('titulo', 'cuerpo')
    filter_horizontal = ('etiquetas',)
    autocomplete_fields = ('autor',)
    inlines = [ImagenArticuloInline]

@admin.register(ImagenArticulo)
class ImagenArticuloAdmin(admin.ModelAdmin):
    list_display = ('articulo', 'imagen', 'descripcion')
    search_fields = ('descripcion', 'articulo__titulo')
