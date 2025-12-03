from django.urls import path
from . import views

app_name = 'tarjetas'

urlpatterns = [
    
    path('listar_tarjetas_fauna/', views.Listar_Tarjetas_Fauna.as_view(), name = 'path_listar_tarjetas_fauna'),
    path('listar_tarjetas_flora/', views.Listar_Tarjetas_Flora.as_view(), name = 'path_listar_tarjetas_flora'),
]