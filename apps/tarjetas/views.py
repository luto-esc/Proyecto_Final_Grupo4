from django.shortcuts import render

# Create your views here.
from .models import Tarjeta_Fauna, Tarjeta_Flora
from django.views.generic import ListView, DetailView

class Listar_Tarjetas_Fauna(ListView):
	model = Tarjeta_Fauna
	template_name = 'tarjetas/lista_tarjetas_fauna.html'
	context_object_name = 'tarjetas_fauna'

class Listar_Tarjetas_Flora(ListView):
	model = Tarjeta_Flora
	template_name = 'tarjetas/lista_tarjetas_flora.html'
	context_object_name = 'tarjetas_flora'

class Detalle_Tarjetas_Fauna(DetailView):
	model = Tarjeta_Fauna
	template_name = 'tarjetas/detalle_tarjetas_fauna.html'
	context_object_name = 'tarjetas_fauna'