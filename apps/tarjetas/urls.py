from django.urls import path
from . import views

app_name = 'tarjetas'

urlpatterns = [
    
    path('listar_tarjetas/', views.listar_tarjetas, name = 'path_listar_tarjetas'),

    path('detalle/<int:pk>', views.Detalle_Tarjeta.as_view(), name = 'path_detalle_tarjeta'),
    
    path('crear_tarjeta/', views.Crear_Tarjeta.as_view(), name = 'path_crear_tarjeta'),

    path('actualizar_tarjeta/<int:pk>', views.Actualizar_Tarjeta.as_view(), name = 'path_actualizar_tarjeta'),

    path('eliminar_tarjeta/<int:pk>', views.Eliminar_Tarjeta.as_view(), name = 'path_eliminar_tarjeta'),

    path('filtro_categoria/<int:pk>', views.filtro_categoria, name = 'path_filtrados_categoria'),    
]