from django.shortcuts import render, HttpResponseRedirect
from apps.posts.models import Post
from apps.categorias.models import Categoria_Sobre
from apps.tarjetas.models import Tarjeta


def Home(request):
    todos_posts = Post.objects.all()
    categorias = Categoria_Sobre.objects.all()
    tarjetas = Tarjeta.objects.all()

    context = {}
    context['posts'] = todos_posts
    context['categorias'] = categorias
    context['tarjetas'] = tarjetas

    return render(request, 'home.html', context)

def MapaDelSitio(request):
    todos_posts = Post.objects.order_by("titulo")
    categorias = Categoria_Sobre.objects.order_by("sobre")
    tarjetas = Tarjeta.objects.order_by("nombre")

    context = {}
    context['posts'] = todos_posts
    context['categorias'] = categorias
    context['tarjetas'] = tarjetas

    return render(request, 'mapa_del_sitio.html', context)