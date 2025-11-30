from django.db import models


# py manage.py makemigrations
# py manage.py migrate

class Post(models.Model):

	titulo = models.TextField(max_length = 1000)
	cuerpo = models.TextField()
	imagen = models.ImageField(upload_to = 'posts_fotos')

	def __str__(self):
		return self.titulo