from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('listar_posts/', views.Listar_Posts.as_view(), name = 'path_listar_posts'),
]