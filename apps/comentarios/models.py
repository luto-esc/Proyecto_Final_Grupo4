from django.db import models
from django.contrib.auth.models import User
from apps.posts.models import Post
# Create your models here.

class Comentario(models.Model):
	fecha_creado = models.DateTimeField(auto_now_add = True)
	fecha_modificado = models.DateTimeField(auto_now = True)
	texto = models.TextField()
	usuario = models.ForeignKey(User, on_delete = models.CASCADE)
	post = models.ForeignKey(Post, on_delete = models.CASCADE)

	def __str__(self):
		return self.fecha_creado

