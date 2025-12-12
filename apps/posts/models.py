from django.db import models


# py manage.py makemigrations
# py manage.py migrate

from apps.categorias.models import Categoria_Sobre

class Post(models.Model):

	titulo = models.CharField(max_length = 200)
	descripcion = models.TextField(default= None)
	cuerpo = models.TextField(default = None)
	fecha = models.DateField(auto_now_add=True)
	imagen = models.ImageField(upload_to = 'posts_fotos')
	categoria_sobre = models.ManyToManyField(Categoria_Sobre)

	def __str__(self):
		return self.titulo