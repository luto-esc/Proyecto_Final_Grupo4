from django.shortcuts import render

# Create your views here.
from .models import Tarjeta
from apps.categorias.models import Categoria_Sobre
from .forms import FormularioCrearActualizarTarjeta
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin


#------------------LISTAR-------------------
def listar_tarjetas(request):
	todas_tarjetas = Tarjeta.objects.all()
	context = {}
	context['tarjetas'] = todas_tarjetas
	
	return render(request,'tarjetas/lista_tarjetas.html', context)

#------------------DETALLE-------------------

class Detalle_Tarjeta(DetailView):
	model = Tarjeta
	template_name = 'tarjetas/detalle_tarjeta.html'
	context_object_name = 'tarjetas'

#------------------CREAR---------STAFFUSERS----------

class Crear_Tarjeta(UserPassesTestMixin, CreateView):
	model = Tarjeta
	template_name = 'tarjetas/crear_tarjeta.html'
	form_class = FormularioCrearActualizarTarjeta
	success_url = reverse_lazy('tarjetas:path_listar_tarjetas')

	def test_func(self):
		if self.request.user.is_staff:
			return True
		else:
			return False	

#------------------ACTUALIZAR---------STAFFUSERS----------
class Actualizar_Tarjeta(UserPassesTestMixin, UpdateView):
	model = Tarjeta
	template_name = 'tarjetas/actualizar_tarjeta.html'
	form_class = FormularioCrearActualizarTarjeta
	success_url = reverse_lazy('tarjetas:path_listar_tarjetas')
	
	def test_func(self):
		if self.request.user.is_staff:
			return True
		else:
			return False

#------------------ELIMINAR---------STAFFUSERS----------
class Eliminar_Tarjeta(UserPassesTestMixin, DeleteView):
	model = Tarjeta
	template_name = 'tarjetas/eliminar_tarjeta.html'
	success_url = reverse_lazy('tarjetas:path_listar_tarjetas')

	def test_func(self):
		if self.request.user.is_staff:
			return True
		else:
			return False

#------------------FILTRO-------------------
def filtro_categoria(request,pk):
	c = Categoria_Sobre.objects.get(pk = pk)

	t = Tarjeta.objects.filter(categoria = c)	
	
	context = {}
	
	context['tarjetas'] = t
	
	categorias = Categoria_Sobre.objects.all()
	
	context['categorias'] = categorias
	
	return render(request,'tarjetas/lista_tarjetas.html', context)
