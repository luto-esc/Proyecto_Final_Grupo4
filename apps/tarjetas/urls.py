from django.urls import path
from . import views

app_name = 'tarjetas'

urlpatterns = [
    
    path('listar_tarjetas_fauna/', views.Listar_Tarjetas_Fauna.as_view(), name = 'path_listar_tarjetas_fauna'),
    path('listar_tarjetas_flora/', views.Listar_Tarjetas_Flora.as_view(), name = 'path_listar_tarjetas_flora'),

    path('detalle_fauna/<int:pk>', views.Detalle_Tarjetas_Fauna.as_view(), name = 'path_detalle_tarjeta_fauna'),
    path('detalle_flora/<int:pk>', views.Detalle_Tarjetas_Flora.as_view(), name = 'path_detalle_tarjeta_flora'),
    
    path('crear_tarjeta_fauna/', views.Crear_Tarjeta_Fauna.as_view(), name = 'path_crear_tarjeta_fauna'),
    path('crear_tarjeta_flora/', views.Crear_Tarjeta_Flora.as_view(), name = 'path_crear_tarjeta_flora'),

    path('actualizar_tarjeta_fauna/<int:pk>', views.Actualizar_Tarjeta_Fauna.as_view(), name = 'path_actualizar_tarjeta_fauna'),
    path('actualizar_tarjeta_flora/<int:pk>', views.Actualizar_Tarjeta_Flora.as_view(), name = 'path_actualizar_tarjeta_flora'),

    path('eliminar_tarjeta_flora/<int:pk>', views.Eliminar_Tarjeta_Flora.as_view(), name = 'path_eliminar_tarjeta_flora'),
    path('eliminar_tarjeta_fauna/<int:pk>', views.Eliminar_Tarjeta_Fauna.as_view(), name = 'path_eliminar_tarjeta_fauna'),    
]