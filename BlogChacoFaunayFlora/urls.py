"""
URL configuration for BlogChacoFaunayFlora project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
    path('posts/', include('apps.posts.urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #Permite que las imagenes que son dinamicas se muestren en el navegador
