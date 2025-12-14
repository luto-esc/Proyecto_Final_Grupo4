from django.urls import path
from . import views

app_name = 'comentarios'

urlpatterns = [
    path('comentar/<int:pk>', views.comentar, name='path_comentar'),

    path('eliminar_comentario/<int:pk>', views.Eliminar_Comentario.as_view(), name = 'path_eliminar_comentario'),

    path('actualizar_comentario/<int:pk>', views.Actualizar_Comentario.as_view(), name = 'path_actualizar_comentario'),
]