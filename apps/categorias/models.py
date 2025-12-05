from django.db import models

# Create your models here.




#///////////// CATEGORIA POST /////////////////////////

class Categoria_Sobre(models.Model):

	sobre = models.CharField(max_length = 100)
	
	def __str__(self):
		return self.sobre

#///////////// CATEGORIA POST /////////////////////////



#///////////// CATEGORIAS DE FAUNA /////////////////////////
class Categoria_Fauna_Clase(models.Model):
	
	clase = models.CharField(max_length = 100)

	def __str__(self):
		return self.clase

class Categoria_Fauna_Dieta(models.Model):
	
	dieta = models.CharField(max_length = 100)

	def __str__(self):
		return self.dieta

class Categoria_Fauna_Estado(models.Model):
	
	estado = models.CharField(max_length = 100)

	def __str__(self):
		return self.estado

#///////////// CATEGORIAS DE FAUNA /////////////////////////


#///////////// CATEGORIAS DE FLORA /////////////////////////
class Categoria_Flora_Tipo(models.Model):
	
	tipo = models.CharField(max_length = 100)

	def __str__(self):
		return self.tipo

class Categoria_Flora_Hambiente(models.Model):
	
	hambiente = models.CharField(max_length = 100)

	def __str__(self):
		return self.hambiente

class Categoria_Flora_Origen(models.Model):
	
	origen = models.CharField(max_length = 100)

	def __str__(self):
		return self.origen

#///////////// CATEGORIAS DE FLORA /////////////////////////

