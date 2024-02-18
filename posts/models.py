from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
    



class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Relación con el modelo User
    # Puedes agregar otros campos como categoría, imagen_principal, etc.

class Comment(models.Model):
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Relación con el modelo User
    article = models.ForeignKey(Article, on_delete=models.CASCADE)  # Relación con el modelo Article
