from django.contrib import admin

# Register your models here.

from .models import Tarjeta_Fauna, Tarjeta_Flora

admin.site.register(Tarjeta_Fauna)
admin.site.register(Tarjeta_Flora)