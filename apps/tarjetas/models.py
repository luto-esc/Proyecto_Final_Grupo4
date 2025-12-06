from django.db import models

# Create your models here.

from apps.categorias.models import Categoria_Fauna, Categoria_Flora



class Tarjeta_Flora(models.Model):

	nombre = models.CharField(max_length = 100)
	descripcion = models.TextField(default="Sin descripción")
	imagen = models.ImageField(upload_to = 'tarjetas_flora_fotos')
	categoria = models.ManyToManyField(Categoria_Flora)

	def __str__(self):
		return self.nombre



class Tarjeta_Fauna(models.Model):

	nombre = models.CharField(max_length = 100)
	descripcion = models.TextField(default="Sin descripción")
	imagen = models.ImageField(upload_to = 'tarjetas_fauna_fotos')
	categoria = models.ManyToManyField(Categoria_Fauna)

	def __str__(self):
		return self.nombre