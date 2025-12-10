from django.shortcuts import render

# Create your views here.
from .models import Tarjeta
from apps.categorias.models import Categoria_Sobre
from .forms import FormularioCrearActualizarTarjeta
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

#------------------LISTAR-------------------
def listar_tarjetas(request):
	todas_tarjetas = Tarjeta.objects.all()
	context = {}
	context['tarjetas'] = todas_tarjetas

	categorias = Categoria_Sobre.objects.all()
	context['categorias'] = categorias
	
	return render(request,'tarjetas/lista_tarjetas.html', context)

#------------------DETALLE-------------------

class Detalle_Tarjeta(DetailView):
	model = Tarjeta
	template_name = 'tarjetas/detalle_tarjeta.html'
	context_object_name = 'tarjetas'

#------------------CREAR-------------------

class Crear_Tarjeta(CreateView):
	model = Tarjeta
	template_name = 'tarjetas/crear_tarjeta.html'
	form_class = FormularioCrearActualizarTarjeta
	success_url = reverse_lazy('tarjetas:path_listar_tarjetas')

#------------------Actualizar-------------------
class Actualizar_Tarjeta(CreateView):
	model = Tarjeta
	template_name = 'tarjetas/actualizar_tarjeta.html'
	form_class = FormularioCrearActualizarTarjeta
	success_url = reverse_lazy('tarjetas:path_listar_tarjetas')

#------------------ELIMINAR-------------------
class Eliminar_Tarjeta(DeleteView):
	model = Tarjeta
	template_name = 'tarjetas/eliminar_tarjeta.html'
	success_url = reverse_lazy('tarjetas:path_listar_tarjetas')

#------------------FILTRO-------------------
def filtro_categoria(request,pk):
	c = Categoria_Sobre.objects.get(pk = pk)

	t = Tarjeta.objects.filter(categoria = c)	
	
	context = {}
	
	context['tarjetas'] = t
	
	categorias = Categoria_Sobre.objects.all()
	
	context['categorias'] = categorias
	
	return render(request,'tarjetas/lista_tarjetas.html', context)
