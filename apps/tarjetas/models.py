from django.db import models

# Create your models here.

from apps.categorias.models import (
    Categoria_Fauna_Clase,
    Categoria_Fauna_Dieta,
    Categoria_Fauna_Estado,
    Categoria_Flora_Tipo,
    Categoria_Flora_Hambiente,
    Categoria_Flora_Origen,
)



class Tarjeta_Flora(models.Model):

	nombre = models.CharField(max_length = 100)
	descripcion = models.TextField(default="Sin descripción")
	imagen = models.ImageField(upload_to = 'tarjetas_flora_fotos')
	categoria_tipo = models.ForeignKey(Categoria_Flora_Tipo, on_delete = models.CASCADE, null = True)
	categoria_hambiente = models.ManyToManyField(Categoria_Flora_Hambiente)
	categoria_origen = models.ForeignKey(Categoria_Flora_Origen, on_delete = models.CASCADE, null = True)

	def __str__(self):
		return self.nombre



class Tarjeta_Fauna(models.Model):

	nombre = models.CharField(max_length = 100)
	descripcion = models.TextField(default="Sin descripción")
	imagen = models.ImageField(upload_to = 'tarjetas_fauna_fotos')
	categoria_clase = models.ForeignKey(Categoria_Fauna_Clase, on_delete = models.CASCADE, null = True)
	categoria_dieta = models.ManyToManyField(Categoria_Fauna_Dieta)
	categoria_estado = models.ManyToManyField(Categoria_Fauna_Estado)

	def __str__(self):
		return self.nombre