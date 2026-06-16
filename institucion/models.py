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
        todos_los_guias = self.guias.all()
        if len(todos_los_guias) == 0:
            return "Sin guías asignados"

        mayor_experiencia = 0
        for guia in todos_los_guias:
            if guia.anios_experiencia_guia > mayor_experiencia:
                mayor_experiencia = guia.anios_experiencia_guia
                
        nombres_ganadores = []
        for guia in todos_los_guias:
            if guia.anios_experiencia_guia == mayor_experiencia:
                nombres_ganadores.append(guia.nombre_completo)
                
        return ", ".join(nombres_ganadores)

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
        return "%s %d %f %s " % (self.titulo_exhibicion, self.duracion_meses,\
            self.costo_produccion, self.tematica)
    