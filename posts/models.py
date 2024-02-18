from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
    


class Archivo(models.Model):
    titulo = models.CharField(max_length=200)
    archivo = models.FileField(upload_to='archivos/') 

    def __str__(self):
        return self.titulo

class Imagen(models.Model):
    titulo = models.CharField(max_length=200)
    cover = models.ImageField(upload_to='images/')

class Texto(models.Model):
    texto = models.TextField()    

class Contenido(models.Model):
    texto = models.ForeignKey(Texto, on_delete= models.SET_NULL, null=True)
    imagen = models.ForeignKey(Imagen,on_delete= models.SET_NULL,null=True)


class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    introduccion = models.TextField()
    contenido = models.ForeignKey(Texto, on_delete= models.SET_NULL,null=True)
  
    publication_date = models.DateTimeField(auto_now_add=True)

    # Puedes agregar otros campos como categoría, imagen_principal, etc.
