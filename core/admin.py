from django.contrib import admin
from .models import Noticia, ImagenGaleria, Descarga
from .models import MensajeContacto

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha')
    list_editable = ('fecha',)
    date_hierarchy = 'fecha'
    search_fields = ('titulo', 'contenido', 'fecha')

@admin.register(ImagenGaleria)
class ImagenGaleriaAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
    search_fields = ('titulo',)

@admin.register(Descarga)
class DescargaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo')
    search_fields = ('nombre',)

@admin.register(MensajeContacto)
class MensajeContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'fecha_envio')
    search_fields = ('nombre', 'correo', 'mensaje')
    ordering = ('-fecha_envio',)
