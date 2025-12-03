from django.db import models

# Create your models here.

class Tarjeta_Flora(models.Model):

	nombre = models.CharField(max_length = 100)
	descripcion = models.TextField()
	imagen = models.ImageField(upload_to = 'tarjetas_flora_fotos')
	nativa = models.BooleanField(default = False) #Por default no es nativa
	toxica = models.BooleanField(default = False) #Por default no es toxica
#	categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE, null = True) #Proximamente a agregar categorias

	def __str__(self):
		return self.nombre



class Tarjeta_Fauna(models.Model):

	nombre = models.CharField(max_length = 100)
	descripcion = models.TextField()
	imagen = models.ImageField(upload_to = 'tarjetas_fauna_fotos')
	estado = models.BooleanField(default = False) #Por default no esta en peligro

	def __str__(self):
		return self.nombre