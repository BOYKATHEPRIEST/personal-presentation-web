from django.contrib import admin
from django.urls import path
from core import views as core_views
from portfolio import views as portafolio_views
from django.conf import settings

"""
Esto no es mas que simples paths que hacen la conecion entre
peticion y el recurso que quieren acceder, en este proyecto no se
usó el metodo POST, solo GET
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.home, name='home'),
    path('about-me/', core_views.about, name='about'),
    path('contacto', core_views.contacto, name='contacto'),
    path('portafolio', portafolio_views.portafolio, name='portafolio'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
