from django.contrib import admin

# Register your models here.
from .models import Museo, GuiaMuseo, Exhibicion

class MuseoAdmin(admin.ModelAdmin):
    list_display = (
        'nombre', 
        'ciudad', 
        'anio_fundacion', 
        'costo_total_produccion',       
        'guias_mas_experimentados'       
    )

class GuiaMuseoAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'anios_experiencia_guia', 'idiomas_hablados', 'museo')
    

class ExhibicionAdmin(admin.ModelAdmin):
    list_display = ('titulo_exhibicion', 'duracion_meses', 'costo_produccion', 'tematica', 'guia')
