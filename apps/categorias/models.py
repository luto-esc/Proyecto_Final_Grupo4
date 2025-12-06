from django.db import models

# Create your models here.




#///////////// CATEGORIA POST /////////////////////////

class Categoria_Sobre(models.Model):

	sobre = models.CharField(max_length = 100)
	descripcion = models.TextField(default="Sin descripción")
	
	def __str__(self):
		return self.sobre

#///////////// CATEGORIA POST /////////////////////////



#///////////// CATEGORIAS DE FAUNA /////////////////////////
class Categoria_Fauna(models.Model):
	
	nombre = models.CharField(max_length = 100)
	descripcion = models.TextField(default="Sin descripción")

	def __str__(self):
		return self.nombre

#///////////// CATEGORIAS DE FAUNA /////////////////////////


#///////////// CATEGORIAS DE FLORA /////////////////////////
class Categoria_Flora(models.Model):
	
	nombre = models.CharField(max_length = 100)
	descripcion = models.TextField(default="Sin descripción")

	def __str__(self):
		return self.nombre

#///////////// CATEGORIAS DE FLORA /////////////////////////

