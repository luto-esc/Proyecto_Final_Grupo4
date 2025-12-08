from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('listar_posts/', views.Listar_Posts_Fun, name = 'path_listar_posts'),
    path('crear_post/', views.Crear_Post.as_view(), name = 'path_crear_post'),
    path('actualizar_post/<int:pk>', views.Actualizar_Post.as_view(), name = 'path_actualizar_post'),
    path('eliminar_post/<int:pk>', views.Eliminar_Post.as_view(), name = 'path_eliminar_post'),
    path('filtro_categoria/<int:pk>', views.Filtro_Post, name = 'path_filtrados_categoria_post'),
]