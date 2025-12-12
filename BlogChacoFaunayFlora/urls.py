from django.contrib import admin
from django.urls import path, include
from . import views #Importamos views

#Importamos para las imagenes
from django.conf import settings #Estas dos lineas son necesarias para que,
from django.conf.urls.static import static # las imagenes cargen


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.Home, name = 'path_home'), #Post
    path('contacto/', views.Contacto, name = 'path_contacto'), #Contacto
    path('nosotros/', views.Nosotros, name = 'path_nosotros'), #Nosotros
    path('posts/', include('apps.posts.urls')),
    path('animales/', include('apps.tarjetas.urls')),
    path('categorias/', include('apps.categorias.urls')),
    path('usuarios/', include('apps.usuarios.urls')),
    path('comentarios/', include('apps.comentarios.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #Permite que las imagenes que son dinamicas se muestren en el navegador
