from django.urls import path
from . import views

app_name = 'categorias'

urlpatterns = [
    
    path('listar_categorias/', views.listar_categorias, name = 'path_listar_categorias'),

    path('detalle/<int:pk>', views.Detalle_Categoria.as_view(), name = 'path_detalle_categoria'),
    
    path('crear_categoria/', views.Crear_Categoria.as_view(), name = 'path_crear_categoria'),

    path('actualizar_categoria/<int:pk>', views.Actualizar_Categoria.as_view(), name = 'path_actualizar_categoria'),

    path('eliminar_categoria/<int:pk>', views.Eliminar_Categoria.as_view(), name = 'path_eliminar_categoria'),

    path('filtrado_categoria_todo/<int:pk>', views.filtro_categoria_todo, name = 'path_filtrado_categoria_todo'),
   
]