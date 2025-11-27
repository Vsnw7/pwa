from django.db import models
from ckeditor.fields import RichTextField

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = RichTextField()
    imagen = models.ImageField(upload_to='noticias/', blank=True, null=True)
    fecha = models.DateField()

    class Meta:
        ordering = ['-fecha']

    def __str__(self):
        return self.titulo


class ImagenGaleria(models.Model):
    titulo = models.CharField(max_length=150)
    imagen = models.ImageField(upload_to='galeria/')
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.titulo


class Descarga(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = RichTextField(blank=True)
    enlace = models.URLField()
    imagen = models.ImageField(upload_to='descargas/', blank=True, null=True)
    idioma = models.CharField(max_length=50, blank=True, null=True)
    requisitosmin = RichTextField(blank=True)
    requisitosmax = RichTextField(blank=True)
    tipo = models.CharField(
        max_length=50,
        choices=[
            ('app', 'Aplicación Móvil'),
            ('game', 'Videojuego'),
        ]
    )

    def __str__(self):
        return f"{self.nombre} ({self.get_tipo_display()})"


class MensajeContacto(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensaje de {self.nombre} ({self.correo})"


