from django import forms
from .models import Tarjeta

class FormularioCrearActualizarTarjeta(forms.ModelForm):

	class Meta:
		model = Tarjeta
		fields = ['nombre', 'descripcion', 'imagen', 'categoria_sobre']