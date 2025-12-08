from .models import Categoria_Sobre, Categoria_Fauna, Categoria_Flora

def categorias_globales_sobre(request):
    return {'categoriassobre': Categoria_Sobre.objects.all()}

def categorias_globales_fauna(request):
    return {'categoriasfauna': Categoria_Fauna.objects.all()}

def categorias_globales_flora(request):
    return {'categoriasflora': Categoria_Flora.objects.all()}