from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),

    # Service Worker 
    path('sw.js', serve, {
        'document_root': settings.BASE_DIR,
        'path': 'sw.js'
    }),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)