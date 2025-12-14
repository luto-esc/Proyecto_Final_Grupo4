from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Contacto

class FormularioRegistroUsuario(UserCreationForm):

	class Meta:
		model = User
		fields = [
			'username',
			'first_name',
			'last_name',
			'email',
			'password1',
			'password2'
			]

class FormularioContacto(forms.ModelForm):
	class Meta:
		model = Contacto
		fields = [
			'nombre_apellido',
			'email',
			'asunto',
			'mensaje'
		]