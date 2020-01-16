from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    """
    Vista que renderiza home.html mediante el metodo request buscando
    por convención en los templates
    """
    return render (request, "core/home.html")

def about(request):
    """
    Vista que renderiza about.html
    """
    return render (request, "core/about.html")

def contacto(request):
    """
    Vista que renderiza contacto
    """
    return render(request, "core/contacto.html")
