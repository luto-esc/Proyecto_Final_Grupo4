from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('listar_posts/', views.listar_posts, name = 'path_listar_posts'),
    
    path('detalle_post/<int:pk>', views.Detalle_Post.as_view(), name = 'path_detalle_post'),
    
    path('crear_post/', views.Crear_Post.as_view(), name = 'path_crear_post'),
    
    path('actualizar_post/<int:pk>', views.Actualizar_Post.as_view(), name = 'path_actualizar_post'),
    
    path('eliminar_post/<int:pk>', views.Eliminar_Post.as_view(), name = 'path_eliminar_post'),
    
    path('filtro_categoria/<int:pk>', views.filtro_post, name = 'path_filtrados_categoria_post'),
]