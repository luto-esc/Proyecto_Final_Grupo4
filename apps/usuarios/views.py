from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import FormularioRegistroUsuario, FormularioContacto
from django.contrib import messages

class RegistroUsuario(CreateView):
	template_name = 'usuarios/registro_usuario.html'
	form_class = FormularioRegistroUsuario
	success_url = reverse_lazy('usuarios:path_login')

class ContactoUsuario(CreateView):
	template_name = 'nosotros.html'
	form_class = FormularioContacto
	success_url = reverse_lazy('usuarios:path_contacto')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['request'] = self.request
		return context

	def form_valid(self, form):
		messages.success(self.request, 'Consulta enviada :)')
		return super().form_valid(form)