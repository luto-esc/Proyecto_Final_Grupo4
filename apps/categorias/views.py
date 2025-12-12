from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

# Create your views here.

from apps.tarjetas.models import Tarjeta
from apps.posts.models import Post
from .models import Categoria_Sobre
from .forms import FormularioCrearActualizarCategoria
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView


#VBC
from django.contrib.auth.mixins import UserPassesTestMixin

#------------------LISTAR-------------------
def listar_categorias(request):
	todas_categorias = Categoria_Sobre.objects.all()
	context = {}
	context['categorias'] = todas_categorias
	
	return render(request,'categorias/lista_categorias.html', context)

#------------------DETALLE-------------------

class Detalle_Categoria(DetailView):
	model = Categoria_Sobre
	template_name = 'categorias/detalle_categoria.html'
	context_object_name = 'categorias'


#------------------CREAR---------STAFFUSERS----------

class Crear_Categoria(UserPassesTestMixin, CreateView):
	model = Categoria_Sobre
	template_name = 'categorias/crear_categoria.html'
	form_class = FormularioCrearActualizarCategoria
	success_url = reverse_lazy('categorias:path_listar_categorias')

	def test_func(self):
		if self.request.user.is_staff:
			return True
		else:
			return False

#------------------Actualizar---------STAFFUSERS----------
class Actualizar_Categoria(UserPassesTestMixin, CreateView):
	model = Categoria_Sobre
	template_name = 'categorias/actualizar_categorias.html'
	form_class = FormularioCrearActualizarCategoria
	success_url = reverse_lazy('tarjetas:path_listar_categorias')

	def test_func(self):
		if self.request.user.is_staff:
			return True
		else:
			return False

#------------------ELIMINAR---------STAFFUSERS----------
class Eliminar_Categoria(UserPassesTestMixin, DeleteView):
	model = Categoria_Sobre
	template_name = 'categorias/eliminar_categoria.html'
	success_url = reverse_lazy('tarjetas:path_listar_categorias')

	def test_func(self):
		if self.request.user.is_staff:
			return True
		else:
			return False


#------------------FILTROXTODO-------------------
def filtro_categoria_todo(request,pk):
	
	c = Categoria_Sobre.objects.get(pk = pk)
	cat = Categoria_Sobre.objects.get(pk = pk)

	p = Post.objects.filter(categoria_sobre = c)
	t = Tarjeta.objects.filter(categoria_sobre = c)
	
	
	context = {}
	
	context['posts'] = p
	context['tarjetas'] = t
	context['cat'] = cat
	
	categorias = Categoria_Sobre.objects.all()
	
	context['categorias'] = categorias
	

	return render(request,'categoriaxpostxtarjeta/detalle_categoria_lista_posts_tarjetas.html', context)



