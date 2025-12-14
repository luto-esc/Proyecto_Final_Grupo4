from django import forms
from .models import Post

class FormularioCrearActualizarPost(forms.ModelForm):

	class Meta:
		model = Post
		fields = ['titulo', 'descripcion', 'cuerpo', 'imagen', 'categoria_sobre']
