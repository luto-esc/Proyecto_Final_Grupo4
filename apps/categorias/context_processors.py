from .models import Categoria_Sobre

def categorias_globales(request):
    return {'categorias': Categoria_Sobre.objects.all()}