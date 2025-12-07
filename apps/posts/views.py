from django.shortcuts import render

# Create your views here.

from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import FormularioCrearPost, FormularioActualizarPost
from apps.categorias.models import Categoria_Sobre

class Listar_Posts(ListView):
	model = Post
	template_name = 'posts/lista_posts.html'
	context_object_name = 'posts'


class Crear_Post(CreateView):
	model = Post
	template_name = 'posts/crear_post.html'
	form_class = FormularioCrearPost
	success_url = reverse_lazy('posts:path_listar_posts')

class Actualizar_Post(UpdateView):
	model = Post
	template_name = 'posts/actualizar_post.html'
	form_class = FormularioActualizarPost
	success_url = reverse_lazy('posts:path_listar_posts')

class Eliminar_Post(DeleteView):
	model = Post
	template_name = 'posts/eliminar_post.html'
	success_url = reverse_lazy('posts:path_listar_posts')

def Filtro_Post(request,pk):
	c = Categoria_Sobre.objects.get(pk = pk)

	p = Post.objects.filter(categorias = c)
	
	context = {}
	
	context['posts'] = p
	
	categorias = Categoria_Sobre.objects.all()
	
	context['categorias'] = categorias
	
	return render(request,'posts/lista_posts.html', context)

