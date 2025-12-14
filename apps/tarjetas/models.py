from django.db import models
from apps.categorias.models import Categoria_Sobre


class Tarjeta(models.Model):

	nombre = models.CharField(max_length = 100)
	descripcion = models.TextField(default="Sin descripción")
	imagen = models.ImageField(upload_to = 'tarjetas_fotos')
	categoria_sobre = models.ManyToManyField(Categoria_Sobre)

	def __str__(self):
		return self.nombre
