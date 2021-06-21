from django.db import models
from .DetalleExposicion import DetalleExposicion
from .Empleado import Empleado

class Exposicion(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_fin = models.DateField()
    fecha_fin_replanificada = models.DateField()
    fecha_inicio = models.DateField()
    fecha_inicio_replanificada = models.DateField()
    hora_apertura = models.DateField()
    hora_cierre = models.DateField()
    detalles_exposicion = models.ForeignKey(DetalleExposicion, on_delete=models.CASCADE,null=True)
    empleado_creo = models.ForeignKey(Empleado, on_delete=models.CASCADE, null=True)

    #MetodosClaseExposicion
    def calcularDuracionObrasExpuestas(self):
        for d in self.detalles_exposicion:
            duracion_obras = d.BuscarDuracionObra()
        return duracion_obras

    def esVigente(self):
        exposiciones_vigentes = Exposicion.objects.get("poner condicion que permita extraer las exp vigentes")
        return exposiciones_vigentes


