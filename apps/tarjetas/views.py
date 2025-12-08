from django.shortcuts import render

# Create your views here.
from .models import Tarjeta_Fauna, Tarjeta_Flora
from apps.categorias.models import Categoria_Fauna, Categoria_Flora
from .forms import FormularioCrearActualizarTarjetaFauna, FormularioCrearActualizarTarjetaFlora
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

#------------------LISTAR-------------------
def Listar_Tarjetas_Fauna_Fun(request):
	todas_tarjetas = Tarjeta_Fauna.objects.all()
	context = {}
	context['tarjetas'] = todas_tarjetas

	categorias = Categoria_Fauna.objects.all()
	context['categorias'] = categorias
	
	return render(request,'tarjetas/lista_tarjetas_fauna.html', context)

def Listar_Tarjetas_Flora_Fun(request):
	todas_tarjetas = Tarjeta_Flora.objects.all()
	context = {}
	context['tarjetas'] = todas_tarjetas

	categorias = Categoria_Flora.objects.all()
	context['categorias'] = categorias
	
	return render(request,'tarjetas/lista_tarjetas_flora.html', context)

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
	success_url = reverse_lazy('tarjetas:path_listar_tarjetas_fauna')

class Crear_Tarjeta_Flora(CreateView):
	model = Tarjeta_Flora
	template_name = 'tarjetas/crear_tarjeta_flora.html'
	form_class = FormularioCrearActualizarTarjetaFlora
	success_url = reverse_lazy('tarjetas:path_listar_tarjetas_flora')

#------------------Actualizar-------------------
class Actualizar_Tarjeta_Fauna(CreateView):
	model = Tarjeta_Fauna
	template_name = 'tarjetas/actualizar_tarjeta_fauna.html'
	form_class = FormularioCrearActualizarTarjetaFauna
	success_url = reverse_lazy('tarjetas:path_listar_tarjetas_fauna')

class Actualizar_Tarjeta_Flora(CreateView):
	model = Tarjeta_Flora
	template_name = 'tarjetas/actualizar_tarjeta_flora.html'
	form_class = FormularioCrearActualizarTarjetaFlora
	success_url = reverse_lazy('tarjetas:path_listar_tarjetas_flora')

#------------------ELIMINAR-------------------
class Eliminar_Tarjeta_Fauna(DeleteView):
	model = Tarjeta_Fauna
	template_name = 'tarjetas/eliminar_tarjeta_fauna.html'
	success_url = reverse_lazy('tarjetas:path_listar_tarjetas_fauna')

class Eliminar_Tarjeta_Flora(DeleteView):
	model = Tarjeta_Flora
	template_name = 'tarjetas/eliminar_tarjeta_flora.html'
	success_url = reverse_lazy('tarjetas:path_listar_tarjetas_flora')

#------------------FILTRO-------------------
def Filtro_Categoria_Fauna(request,pk):
	c = Categoria_Fauna.objects.get(pk = pk)

	t = Tarjeta_Fauna.objects.filter(categoria = c)	
	
	context = {}
	
	context['tarjetas'] = t
	
	categorias = Categoria_Fauna.objects.all()
	
	context['categorias'] = categorias
	
	return render(request,'tarjetas/lista_tarjetas_fauna.html', context)

def Filtro_Categoria_Flora(request,pk):
	c = Categoria_Flora.objects.get(pk = pk)

	t = Tarjeta_Flora.objects.filter(categoria = c)	
	
	context = {}
	
	context['tarjetas'] = t
	
	categorias = Categoria_Flora.objects.all()
	
	context['categorias'] = categorias
	
	return render(request,'tarjetas/lista_tarjetas_flora.html', context)