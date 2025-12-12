from django.shortcuts import render

# Create your views here.

from .models import Post
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .forms import FormularioCrearPost, FormularioActualizarPost
from apps.categorias.models import Categoria_Sobre
from django.contrib.auth.mixins import UserPassesTestMixin

#------------------LISTAR-------------------
def listar_posts(request):
	todos_posts = Post.objects.all()
	context = {}
	context['posts'] = todos_posts

	categorias = Categoria_Sobre.objects.all()
	context['categorias'] = categorias
	
	return render(request,'posts/lista_posts.html', context)


#------------------DETALLE-------------------
class Detalle_Post(DetailView):
	model = Post
	template_name = 'posts/detalle_post.html'
	context_object_name = 'posts'

	
#------------------CREAR---------STAFFUSERS----------
class Crear_Post(UserPassesTestMixin, CreateView):
	model = Post
	template_name = 'posts/crear_post.html'
	form_class = FormularioCrearPost
	success_url = reverse_lazy('posts:path_listar_posts')

	def test_func(self):
		if self.request.user.is_staff:
			return True
		else:
			return False

#------------------ACTUALIZAR---------STAFFUSERS----------
class Actualizar_Post(UserPassesTestMixin, UpdateView):
	model = Post
	template_name = 'posts/actualizar_post.html'
	form_class = FormularioActualizarPost
	success_url = reverse_lazy('posts:path_listar_posts')

	def test_func(self):
		if self.request.user.is_staff:
			return True
		else:
			return False

#------------------ELIMINAR---------STAFFUSERS----------
class Eliminar_Post(UserPassesTestMixin, DeleteView):
	model = Post
	template_name = 'posts/eliminar_post.html'
	success_url = reverse_lazy('posts:path_listar_posts')

	def test_func(self):
		if self.request.user.is_staff:
			return True
		else:
			return False

#------------------FILTRO-------------------
def filtro_post(request,pk):
	c = Categoria_Sobre.objects.get(pk = pk)

	p = Post.objects.filter(categoria_sobre = c)	
	
	context = {}
	
	context['posts'] = p
	
	categorias = Categoria_Sobre.objects.all()
	
	context['categorias'] = categorias
	
	return render(request,'posts/lista_posts.html', context)

