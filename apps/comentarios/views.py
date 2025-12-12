from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User
from apps.posts.models import Post
from apps.comentarios.models import Comentario
from django.contrib.auth.decorators import login_required

@login_required
def comentar(request, pk):
	p = Post.objects.get(pk = pk)
	u = request.user

	c = request.POST.get('texto_comentado', None)
	Comentario.objects.create(texto = c, usuario = u, producto = c)


