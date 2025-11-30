from django.shortcuts import render

# Create your views here.

from .models import Post
from django.views.generic import ListView

class Listar_Posts(ListView):
	model = Post
	template_name = 'posts/lista_posts.html'
	context_object_name = 'posts'