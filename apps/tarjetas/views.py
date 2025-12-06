from django.shortcuts import render

# Create your views here.
from .models import Tarjeta_Fauna, Tarjeta_Flora
from .forms import FormularioCrearActualizarTarjetaFauna, FormularioCrearActualizarTarjetaFlora
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

#------------------LISTAR-------------------
class Listar_Tarjetas_Fauna(ListView):
	model = Tarjeta_Fauna
	template_name = 'tarjetas/lista_tarjetas_fauna.html'
	context_object_name = 'tarjetas_fauna'

class Listar_Tarjetas_Flora(ListView):
	model = Tarjeta_Flora
	template_name = 'tarjetas/lista_tarjetas_flora.html'
	context_object_name = 'tarjetas_flora'

#------------------DETALLE-------------------

class Detalle_Tarjetas_Fauna(DetailView):
	model = Tarjeta_Fauna
	template_name = 'tarjetas/detalle_tarjetas_fauna.html'
	context_object_name = 'tarjetas_fauna'

class Detalle_Tarjetas_Flora(DetailView):
	model = Tarjeta_Flora
	template_name = 'tarjetas/detalle_tarjetas_fauna.html'
	context_object_name = 'tarjetas_fauna'

#------------------CREAR-------------------

class Crear_Tarjeta_Fauna(CreateView):
	model = Tarjeta_Fauna
	template_name = 'tarjetas/crear_tarjeta_fauna.html'
	form_class = FormularioCrearActualizarTarjetaFauna
	succues_url = reverse_lazy('path_listar_tarjetas_fauna')

class Crear_Tarjeta_Flora(CreateView):
	model = Tarjeta_Flora
	template_name = 'tarjetas/crear_tarjeta_flora.html'
	form_class = FormularioCrearActualizarTarjetaFlora
	succues_url = reverse_lazy('path_listar_tarjetas_flora')

#------------------Actualizar-------------------
class Actualizar_Tarjeta_Fauna(CreateView):
	model = Tarjeta_Fauna
	template_name = 'tarjetas/actualizar_tarjeta_fauna.html'
	form_class = FormularioCrearActualizarTarjetaFauna
	succues_url = reverse_lazy('path_listar_tarjetas_fauna')

class Actualizar_Tarjeta_Flora(CreateView):
	model = Tarjeta_Flora
	template_name = 'tarjetas/actualizar_tarjeta_flora.html'
	form_class = FormularioCrearActualizarTarjetaFlora
	succues_url = reverse_lazy('path_listar_tarjetas_flora')