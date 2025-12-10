from django import forms
from .models import Categoria_Sobre

class FormularioCrearActualizarCategoria(forms.ModelForm):

	class Meta:
		model = Categoria_Sobre
		fields = ['sobre', 'imagen', 'descripcion']