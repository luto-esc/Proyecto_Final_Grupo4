from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from apps.posts.models import Post
from .models import Comentario
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import DeleteView, UpdateView
from .forms import FormularioActualizarComentario



#------------------CREAR-------------------
@login_required
def comentar(request, pk):
	
	p = Post.objects.get(pk = pk)
	u = request.user

	c = request.POST.get('texto_comentado', None)

	Comentario.objects.create(texto = c, usuario = u, post = p)

	return HttpResponseRedirect(reverse_lazy('posts:path_detalle_post', kwargs = {'pk':pk}))


#------------------ELIMINAR----USER-----STAFFUSERS----------
class Eliminar_Comentario(DeleteView):

	model = Comentario
	template_name = 'comentarios/eliminar_comentario.html'
	
	def get_success_url(self):
		return reverse_lazy('posts:path_detalle_post', kwargs={'pk': self.object.post.pk})


#------------------ACTUALIZAR---USER----------------
class Actualizar_Comentario(UpdateView):
	
	model = Comentario
	template_name = 'comentarios/actualizar_comentario.html'
	form_class = FormularioActualizarComentario

	def get_success_url(self):
		return reverse_lazy('posts:path_detalle_post', kwargs={'pk': self.object.post.pk})	