from django.shortcuts import render, HttpResponseRedirect
from apps.posts.models import Post
from apps.categorias.models import Categoria_Sobre

def Home(request):
    
    todos_posts = Post.objects.all()
    context = {}
    context['posts'] = todos_posts

    categorias = Categoria_Sobre.objects.all()
    context['categorias'] = categorias
    return render(request, 'home.html', context)

def Contacto(request):
    return render(request, 'contacto.html')

def Nosotros(request):
    return render(request, 'nosotros.html')