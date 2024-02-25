from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class juegos(models.Model):
    nombre = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    clasificacion = models.IntegerField()
    precio = models.IntegerField()
    
    class Meta:
        verbose_name = "juego"
        verbose_name_plural = "juegos"
        ordering = ['nombre']
    
    def __str__(self):
        return f"{self.nombre}"
        
    
class vendedores(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    numeroV = models.IntegerField() #numero de vendedor
    
    class Meta:
        verbose_name = "vendedor"
        verbose_name_plural = "vendedores"
        ordering = ['numeroV']
    
    def __str__(self):
        return f"{self.nombre}, {self.apellido}"
    
class usuarios(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    
    class Meta:
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"
        ordering = ['nombre']
    
    def __str__(self):
        return f"{self.nombre},  {self.apellido}"
    
class comentarios(models.Model):
    comentario = models.CharField(max_length=280)

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
    
class figuras(models.Model):
    nombre = models.CharField(max_length=50)
    saga = models.CharField(max_length=50) #saga, juego, libro o pelicula a cual pertenezca dicha figura de accion
    precio = models.IntegerField()
    
    class Meta:
        verbose_name = "figura"
        verbose_name_plural = "figuras"
        ordering = ['saga']
    
    def __str__(self):
        return f"{self.nombre}, {self.saga}"
    
class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"  