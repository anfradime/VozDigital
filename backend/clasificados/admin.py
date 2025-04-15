from django.contrib import admin
from .models import CategoriaClasificado, Clasificado, ImagenClasificado, ReporteClasificado, CalificacionVendedor

class ImagenClasificadoInline(admin.TabularInline):
    model = ImagenClasificado
    extra = 1

@admin.register(Clasificado)
class ClasificadoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'usuario', 'categoria', 'precio', 'disponible', 'fecha_publicacion')
    search_fields = ('titulo', 'descripcion', 'usuario__username')
    list_filter = ('categoria', 'disponible')
    inlines = [ImagenClasificadoInline]

admin.site.register(CategoriaClasificado)
admin.site.register(ReporteClasificado)
admin.site.register(CalificacionVendedor)

