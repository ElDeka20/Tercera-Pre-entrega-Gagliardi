from django.db import models
from django.contrib.auth.models import User

class TemaDeDiscusion(models.Model):
    nombre = models.CharField(max_length=100)

class NuevaDiscusion(models.Model):
    tema = models.ForeignKey(TemaDeDiscusion, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()

    def __str__(self):
        return self.titulo