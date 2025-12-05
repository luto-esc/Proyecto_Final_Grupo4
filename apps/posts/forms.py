from django import forms
from .models import Post

class FormularioCrearPost(forms.ModelForm):

	class Meta:
		model = Post
		fields = ['titulo', 'descripcion', 'cuerpo', 'imagen', 'categoria_sobre']

class FormularioActualizarPost(forms.ModelForm):

	class Meta:
		model = Post
		fields = ['titulo', 'descripcion', 'cuerpo', 'imagen', 'categoria_sobre']