from django.db import models

# Create your models here.




#///////////// CATEGORIA/ETIQUETAS /////////////////////////

class Categoria_Sobre(models.Model):

	sobre = models.CharField(max_length = 100)
	imagen = models.ImageField(upload_to = 'categorias_foto')
	descripcion = models.TextField(default="Sin descripción")
	
	def __str__(self):
		return self.sobre

#///////////// CATEGORIA/ETIQUETAS /////////////////////////

