from django.contrib import admin
from .models import Project

# Register your models here.
admin.site.register(Project)
"""
En la linea 5 se está creando un Modelo en el administrador de django,
un 'Proyecto' con todos sus atributos de clase que a su vez, no es más que la
definición de una base de datos que sirve para controlar aquel Modelo.

Pd: se dejó de usar sqlite por fallos en la version de django, así que
me conecté mejor a mysql
"""
