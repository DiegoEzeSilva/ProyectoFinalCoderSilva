from django.contrib import admin
from .models import Empleado, ProductosNuevos, ProductosUsados, Equipamiento, Avatar

# Register your models here.
admin.site.register(Empleado)
admin.site.register(ProductosNuevos)
admin.site.register(ProductosUsados)
admin.site.register(Equipamiento)
admin.site.register(Avatar)