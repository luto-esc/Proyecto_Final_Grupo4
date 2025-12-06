from django import forms
from .models import Tarjeta_Fauna, Tarjeta_Flora

class FormularioCrearActualizarTarjetaFauna(forms.ModelForm):

	class Meta:
		model = Tarjeta_Fauna
		fields = ['nombre', 'descripcion', 'imagen', 'categoria']

class FormularioCrearActualizarTarjetaFlora(forms.ModelForm):

	class Meta:
		model = Tarjeta_Flora
		fields = ['nombre', 'descripcion', 'imagen', 'categoria']
