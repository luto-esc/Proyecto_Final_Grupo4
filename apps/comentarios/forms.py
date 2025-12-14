from django import forms
from .models import Comentario

class FormularioActualizarComentario(forms.ModelForm):

	class Meta:
		model = Comentario
		fields = ['texto']