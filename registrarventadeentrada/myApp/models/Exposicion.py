from django.db import models
from .DetalleExposicion import DetalleExposicion

class Exposicion(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_fin = models.DateField()
    fecha_fin_replanificada = models.DateField()
    fecha_inicio = models.DateField()
    fecha_inicio_replanificada = models.DateField()
    hora_apertura = models.DateField()
    hora_cierre = models.DateField()

    #MetodosClaseExposicion
    def calcularDuracionObrasExpuestas(self):
        detalles = DetalleExposicion.objects.get("poner condicion que establezca la relacion entre la exposicion con sus detalles")
        for d in detalles:
            duracion_obras = detalles.BuscarDuracionObra()
        return duracion_obras

    def esVigente(self):
        exposiciones_vigentes = Exposicion.objects.get("poner condicion que permita extraer las exp vigentes")
        return exposiciones_vigentes

