from django.shortcuts import render

# Create your views here.

from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import FormularioCrearPost, FormularioActualizarPost

class Listar_Posts(ListView):
	model = Post
	template_name = 'posts/lista_posts.html'
	context_object_name = 'posts'


class Crear_Post(CreateView):
	model = Post
	template_name = 'posts/crear_post.html'
	form_class = FormularioCrearPost
	succues_url = reverse_lazy('path_listar_posts')

class Actualizar_Post(UpdateView):
	model = Post
	template_name = 'posts/actualizar_post.html'
	form_class = FormularioActualizarPost
	succues_url = reverse_lazy('path_listar_posts')

class Eliminar_Post(DeleteView):
	model = Post
	template_name = 'posts/eliminar_post.html'
	succues_url = reverse_lazy('path_listar_posts')

