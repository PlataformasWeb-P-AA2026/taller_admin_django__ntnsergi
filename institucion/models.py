from django.db import models

# Create your models here.

class Museo(models.Model):
    nombre = models.CharField("Nombre del Museo", unique=True, null=False)
    ciudad= models.CharField("Ciudad donde se ubica el museo")
    anio_fundacion = models.IntegerField("Año de fundacion")
    
    def __str__(self):
        return "%s %s %f" % (self.nombre, self.ciudad , self.anio_fundacion)

class GuiaMuseo(models.Model):
    nombre_completo = models.CharField("Nombre y Apellido del guia")
    anios_experiencia_guia = models.IntegerField("Años de experiencia")
    idiomas_hablados = models.CharField("Idiomas que puede hablar el guia")
    
    museo = models.ForeignKey(Museo, on_delete=models.CASCADE, related_name="guias")
    
    
    
class Exhibicion(models.Model):
    titulo_exhibicion = models.CharField("Titulo de la exhibicion")
    duaracion_meses = models.IntegerField("Duracion de la exhibicion en meses")
    costo_produccion = models.FloatField("Costo total de la produccion")
    tematica = models.CharField("Tematica proncipal de la exhibicion")
    
    guia = models.ForeignKey(GuiaMuseo, on_delete=models.CASCADE, related_name="exhibiciones")
    