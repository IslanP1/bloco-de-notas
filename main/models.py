from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Notas(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    titulo = models.CharField(max_length=200)
    anotacao = models.TextField()
    
    def __str__(self):
        return self.titulo
    

