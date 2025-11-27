from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Noticia, ImagenGaleria, Descarga, MensajeContacto
from .forms import FormularioContacto

def inicio(request):
    # Manejamos el formulario de contacto
    if request.method == 'POST':
        form = FormularioContacto(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu mensaje ha sido enviado con éxito. ¡Gracias por contactarnos!')
            return redirect('inicio')
    else:
        form = FormularioContacto()

    # Obtenemos las 3 últimas noticias
    noticias = Noticia.objects.all()[:3]

    # Obtenemos los proyectos (descargas tipo 'game')
    proyectos = Descarga.objects.filter(tipo='game')[:3]

    # Contexto para el template
    context = {
        'form': form,
        'noticias': noticias,
        'proyectos': proyectos,
    }

    return render(request, 'core/inicio.html', context)


def noticias(request):
    noticias_list = Noticia.objects.all().order_by('-fecha')
    paginator = Paginator(noticias_list, 6)
    
    page_number = request.GET.get('page')
    noticias_paginadas = paginator.get_page(page_number)
    
    return render(request, 'core/noticias.html', {'noticias': noticias_paginadas})

def galeria(request):
    imagenes_list = ImagenGaleria.objects.all().order_by('-id')
    paginator = Paginator(imagenes_list, 6) 
    
    page_number = request.GET.get('page')
    imagenes_paginadas = paginator.get_page(page_number)
    
    return render(request, 'core/galeria.html', {'imagenes': imagenes_paginadas})

def descargas(request):
    descargas = Descarga.objects.all()
    app = descargas.filter(tipo='app')
    game = descargas.filter(tipo='game')
    return render(request, 'core/descargas.html', {'apps': app, 'juegos': game})