from django.shortcuts import render
from .models import Project
# Create your views here.
def portafolio(request):
    """
    Como buena practica de programación es mejor tener organizado
    el código y renderizar cada template en su app correspondiente
    """
    projects = Project.objects.all()
    return render(request, "portafolio/portafolio.html")
