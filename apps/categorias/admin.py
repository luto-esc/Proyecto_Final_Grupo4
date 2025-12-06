from django.contrib import admin

# Register your models here.
from .models import Categoria_Sobre, Categoria_Fauna, Categoria_Flora

admin.site.register(Categoria_Sobre)
admin.site.register(Categoria_Fauna)
admin.site.register(Categoria_Flora)