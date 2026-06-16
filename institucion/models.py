from django.db import models

# Create your models here.

class Museo(models.Model):
    nombre = models.CharField("Nombre del Museo", unique=True, null=False)
    ciudad= models.CharField("Ciudad donde se ubica el museo")
    anio_fundacion = models.IntegerField("Año de fundacion")
    
    def __str__(self):
        return "%s %s %d" % (self.nombre, self.ciudad , self.anio_fundacion)
    
    def costo_total_produccion(self):
        total = 0
        for guia in self.guias.all():
            for exhibicion in guia.exhibiciones.all():
                total += exhibicion.costo_produccion
        
        return total
    
    def guias_mas_experimentados(self):
        mejor_guia = self.guias.all().order_by('-anios_experiencia_guia').first()
        
        if mejor_guia:
            return mejor_guia.nombre_completo
        else:
            return "No hay texto"

class GuiaMuseo(models.Model):
    nombre_completo = models.CharField("Nombre y Apellido del guia")
    anios_experiencia_guia = models.IntegerField("Años de experiencia")
    idiomas_hablados = models.CharField("Idiomas que puede hablar el guia")
    
    museo = models.ForeignKey(Museo, on_delete=models.CASCADE, related_name="guias")
    
    def __str__(self):
        return "%s %d %s " % (self.nombre_completo, self.anios_experiencia_guia,\
            self.idiomas_hablados)
    
class Exhibicion(models.Model):
    titulo_exhibicion = models.CharField("Titulo de la exhibicion")
    duracion_meses = models.IntegerField("Duracion de la exhibicion en meses")
    costo_produccion = models.FloatField("Costo total de la produccion")
    tematica = models.CharField("Tematica proncipal de la exhibicion")
    
    guia = models.ForeignKey(GuiaMuseo, on_delete=models.CASCADE, \
        related_name="exhibiciones")
    
    def __str__(self):
        return "%s %d %f %s " % (self.titulo_exhibicion, self.duaracion_meses,\
            self.costo_produccion, self.tematica)
    