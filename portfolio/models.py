from django.db import models

# Create your models here.
class Project(models.Model):
    """
    creacion de mi modelo, para modelar se debe de heredar de
    la clasee Model
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="projects")
    created_at = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Nos retorna el titulo que se le asigna en el administrador
        de Djnago
        """
        return self.title
